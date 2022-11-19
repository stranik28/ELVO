from repository.companies import CompaniesRepository
from database.connections import get_database_connection

def get_companies_service() -> CompaniesRepository:
    db = get_database_connection()
    return CompaniesRepository(next(db))
    