from fpdf import FPDF

def generate_pdf_report(patient_id: int, risk_score: float, recommendations: str) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Отчет по пациенту {patient_id}", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(0, 10, txt=f"Риск: {risk_score:.2f}", ln=True)
    pdf.cell(0, 10, txt=f"Рекомендации: {recommendations}", ln=True)
    file_path = f"reports/patient_{patient_id}.pdf"
    pdf.output(file_path)
    return file_path

@router.get("/api/export/{patient_id}", summary="Экспорт анализа в PDF")
async def export_patient_analysis(patient_id: int):
    patient_data = get_patient_data(patient_id)
    if not patient_data:
        raise HTTPException(status_code=404, detail="Данные пациента не найдены")

    input_data = torch.tensor(patient_data["features"], dtype=torch.float32)
    with torch.no_grad():
        prediction = model(input_data)

    risk_score = prediction.item()
    recommendations = "Высокий риск!" if risk_score > 0.7 else "Риск низкий."
    pdf_path = generate_pdf_report(patient_id, risk_score, recommendations)

    return {"message": "Отчет успешно создан", "file_path": pdf_path}
