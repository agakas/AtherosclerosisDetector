from fastapi import FastAPI
from controllers.patient_controller import router as patient_router
from controllers.examination_controller import router as examination_router
from controllers.human_controller import router as human_router
from controllers.doctor_controller import router as doctor_router
from controllers.prescriptions_controller import router as prescriptions_router

app = FastAPI(title="API медицинской системы")

# Подключение роутеров
app.include_router(patient_router)
app.include_router(examination_router)
app.include_router(human_router)
app.include_router(doctor_router)
app.include_router(prescriptions_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)