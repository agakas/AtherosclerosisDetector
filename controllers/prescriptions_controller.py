from fastapi import APIRouter
from services.prescriptions_service import get_prescriptions
from models.prescriptions import Prescription

router = APIRouter()

@router.get('/prescriptions/{patient_id}')
def get_prescriptions_by_patient(patient_id: int):
    # Получение назначений для пациента
    prescriptions = get_prescriptions(patient_id)
    return [Prescription(**presc).__dict__ for presc in prescriptions]