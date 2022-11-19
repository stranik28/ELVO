from repository.reviews import ReviewsRepository
from database.connections import get_database_connection

def get_reviews_service() -> ReviewsRepository:
    db = get_database_connection()
    return ReviewsRepository(next(db))