from repositories.patient_repository import fetch_patient
from ml_models.risk_prediction_model import RiskPredictionModel

# Загрузка новой модели
model = RiskPredictionModel()

def analyze_patient_data(patient_id: int):
    # Получение данных пациента из репозитория
    patient_data = fetch_patient(patient_id)
    if not patient_data:
        raise ValueError("Данные пациента не найдены")

    # Запуск анализа на модели
    risk_score = model.predict(patient_data["features"])
    recommendations = (
        "Высокий риск! Рекомендуется оперативное вмешательство."
        if risk_score > 0.7
        else "Риск низкий. Продолжить консервативное лечение."
    )

    return {
        "patient_id": patient_id,
        "risk_score": risk_score,
        "recommendations": recommendations,
    }
