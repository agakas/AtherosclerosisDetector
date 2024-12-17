from repositories.examination_repository import fetch_examinations

def get_examinations(patient_id: int):
    # Сервис для получения данных обследований
    return fetch_examinations(patient_id)