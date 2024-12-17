from repositories.doctor_repository import fetch_doctor

def get_doctor_data(doctor_id: int):
    # Сервис для получения данных о враче
    return fetch_doctor(doctor_id)