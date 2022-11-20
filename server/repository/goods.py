from repository.base import BaseRepository
from schemas.goods import Goods
from models.goods import goods as GoodsInDB

from passlib.hash import pbkdf2_sha256

from database.connections import get_database_connection

pwd_context = pbkdf2_sha256
pwd_context.using(salt="123".encode('utf-8'))

class GoodsRepository(BaseRepository):
    def get_goods(self):
        return self.session.query(GoodsInDB).all()

    def create_goods(self, goods: Goods):
        hash = pwd_context.hash(str(goods.name))
        goodstodb = goods(name=goods.name, cost=goods.cost, description=goods.description, hash=hash, partner_id=goods.partner_id)
        self.session.add(goodstodb)
        self.session.commit()
        self.session.refresh(goodstodb)

        return goodstodb

    def get_goods_by_id(self, id: int):
        goods = self.session.query(GoodsInDB).filter(GoodsInDB.id == id).first()
        return goods

    def update_goods(self, id: int, goods: Goods):
        goods_in_db = self.session.query(GoodsInDB).filter(GoodsInDB.id == id).first()
        setattr(goods_in_db, 'name', goods.name)
        setattr(goods_in_db, 'cost', goods.cost)
        setattr(goods_in_db, 'description', goods.description)
        setattr(goods_in_db, 'hash', goods.hash)
        setattr(goods_in_db, 'partner_id', goods.partner_id)
        self.session.commit()
        self.session.refresh(goods_in_db)

        return goods_in_db

    def delete_goods(self, id: int):
        goods_in_db = self.session.query(GoodsInDB).filter(GoodsInDB.id == id).first()
        self.session.delete(goods_in_db)
        self.session.commit()
        return True
    
    def verify_goods(self, id: int, hash: str):
        goods_in_db = self.session.query(GoodsInDB).filter(GoodsInDB.id == id).first()
        if goods_in_db.hash == hash:
            return True
        else:
            return False