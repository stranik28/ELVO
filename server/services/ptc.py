from repository.ptc import PTCRepository
from database.connections import get_database_connection

def get_ptc_service() -> PTCRepository:
    db = get_database_connection()
    return PTCRepository(next(db))