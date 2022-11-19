from repository.partners import PartnersRepository
from database.connections import get_database_connection

def get_partners_service() -> PartnersRepository:
    db = get_database_connection()
    return PartnersRepository(next(db))