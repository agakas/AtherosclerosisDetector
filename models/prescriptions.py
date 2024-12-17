class Prescription:
    def __init__(self, id, patient_id, doctor_id, date, recommendation):
        # Модель назначения
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.recommendation = recommendation