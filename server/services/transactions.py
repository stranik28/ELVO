from repository.transactions import TransactionRepository
from database.connections import get_database_connection

def get_transaction_service() -> TransactionRepository:
    db = get_database_connection()
    return TransactionRepository(next(db))