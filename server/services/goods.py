from repository.goods import GoodsRepository
from database.connections import get_database_connection

def get_goods_service() -> GoodsRepository:
    db = get_database_connection()
    return GoodsRepository(next(db))

    