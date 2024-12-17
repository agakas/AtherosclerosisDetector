from fastapi import APIRouter
from services.patient_service import get_patient_data
from models.patient import Patient

router = APIRouter()

@router.get('/patients/{patient_id}')
def get_patient(patient_id: int):
    # Получение данных о пациенте
    patient = get_patient_data(patient_id)
    return Patient(**patient).__dict__