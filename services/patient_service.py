from repositories.patient_repository import fetch_patient

def get_patient_data(patient_id: int):
    # Сервис для получения данных пациента
    return fetch_patient(patient_id)