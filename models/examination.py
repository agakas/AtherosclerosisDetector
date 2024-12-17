class Examination:
    def __init__(self, id, patient_id, date, result):
        # Модель обследования
        self.id = id
        self.patient_id = patient_id
        self.date = date
        self.result = result