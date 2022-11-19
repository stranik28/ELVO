from repository.admin import AdminRepository
from database.connections import get_database_connection

def get_admin_service() -> AdminRepository:
    db = get_database_connection()
    return AdminRepository(next(db))