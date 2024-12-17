from fastapi import APIRouter
from services.examination_service import get_examinations
from models.examination import Examination

router = APIRouter()

@router.get('/examinations/{patient_id}')
def get_examinations_by_patient(patient_id: int):
    # Получение данных об обследованиях пациента
    exams = get_examinations(patient_id)
    return [Examination(**exam).__dict__ for exam in exams]