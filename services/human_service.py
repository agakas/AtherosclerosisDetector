from repositories.human_repository import fetch_human

def get_human_data(human_id: int):
    # Сервис для получения данных о человеке
    return fetch_human(human_id)