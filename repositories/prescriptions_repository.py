def fetch_prescriptions(patient_id: int):
    # Имитация вызова к базе данных для получения назначений пациента
    return [{"id": 1, "patient_id": patient_id, "doctor_id": 202, "date": "2024-06-02", "recommendation": "Принимать аспирин"}]