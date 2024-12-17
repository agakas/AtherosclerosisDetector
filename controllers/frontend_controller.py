from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import torch
from database import get_patient_data, save_recommendations

# Инициализация контроллера
router = APIRouter()

# Pydantic модель для запроса рекомендаций
class PatientAnalysisRequest(BaseModel):
    patient_id: int

# Pydantic модель для сохранения рекомендаций
class RecommendationRequest(BaseModel):
    patient_id: int
    doctor_id: int
    recommendations: str

# Загрузка предобученной модели
model = torch.load('risk_prediction_model.pth')
model.eval()

# GET: Получение анализа данных пациента
@router.get("/api/analysis/{patient_id}", summary="Получить анализ данных пациента")
async def get_patient_analysis(patient_id: int):
    # Получение данных пациента из БД
    patient_data = get_patient_data(patient_id)
    if not patient_data:
        raise HTTPException(status_code=404, detail="Данные пациента не найдены")

    # Подготовка данных для модели
    input_data = torch.tensor(patient_data["features"], dtype=torch.float32)

    # Запуск предсказания
    with torch.no_grad():
        prediction = model(input_data)

    risk_score = prediction.item()

    # Формирование рекомендаций
    if risk_score > 0.7:
        recommendations = "Высокий риск! Рекомендуется срочное обследование и оперативное вмешательство."
    else:
        recommendations = "Риск низкий. Продолжить наблюдение и консервативное лечение."

    # Возвращаем результат на фронтенд
    return {
        "patient_id": patient_id,
        "risk_score": risk_score,
        "recommendations": recommendations
    }

# POST: Сохранение рекомендаций в БД
@router.post("/api/recommendations", summary="Сохранить рекомендации врача")
async def save_recommendation(request: RecommendationRequest):
    try:
        # Сохранение данных в таблицу APPOINTMENTS
        save_recommendations(
            patient_id=request.patient_id,
            doctor_id=request.doctor_id,
            recommendations=request.recommendations
        )
        return {"status": "success", "message": "Рекомендации успешно сохранены"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
