from repositories.prescriptions_repository import fetch_prescriptions

def get_prescriptions(patient_id: int):
    # Сервис для получения данных о назначениях пациента
    return fetch_prescriptions(patient_id)