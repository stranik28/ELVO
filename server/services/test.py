from repository.test import TestRepository
from database.connections import get_database_connection

def get_test_service() -> TestRepository:
    db = get_database_connection()
    return TestRepository(next(db))