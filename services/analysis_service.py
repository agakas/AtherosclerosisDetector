from ml_models.risk_prediction_model import predict_risk
from repositories.patient_repository import fetch_patient
from repositories.examination_repository import fetch_examinations

def analyze_patient_data(patient_id: int):
    # Сервис для анализа данных пациента
    patient = fetch_patient(patient_id)
    examinations = fetch_examinations(patient_id)
    data = {"patient": patient, "examinations": examinations}
    risk_result = predict_risk(data)
    return risk_result