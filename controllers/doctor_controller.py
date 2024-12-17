from fastapi import APIRouter
from services.doctor_service import get_doctor_data
from models.doctor import Doctor

router = APIRouter()

@router.get('/doctors/{doctor_id}')
def get_doctor(doctor_id: int):
    # Получение информации о враче
    doctor = get_doctor_data(doctor_id)
    return Doctor(**doctor).__dict__