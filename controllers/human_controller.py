from fastapi import APIRouter
from services.human_service import get_human_data
from models.human import Human

router = APIRouter()

@router.get('/humans/{human_id}')
def get_human(human_id: int):
    # Получение информации о человеке
    human = get_human_data(human_id)
    return Human(**human).__dict__