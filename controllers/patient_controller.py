from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import logging
from services.analysis_service import analyze_patient_data

# Настройка логирования
logger = logging.getLogger(__name__)

# Инициализация контроллера
router = APIRouter()

# Pydantic модель для анализа данных пациента
class PatientAnalysisRequest(BaseModel):
    patient_id: int

@router.post("/api/analyze", summary="Анализ данных пациента")
async def analyze_patient(request: PatientAnalysisRequest):
    try:
        # Вызов сервиса анализа
        result = analyze_patient_data(request.patient_id)
        logger.info(f"Успешный анализ пациента ID {request.patient_id}: {result}")
        return result
    except ValueError as e:
        logger.error(f"Ошибка анализа пациента ID {request.patient_id}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.critical(f"Системная ошибка при анализе пациента ID {request.patient_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Произошла внутренняя ошибка")
