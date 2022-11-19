from repository.base import BaseRepository
from models.partners import Partners
from schemas.partners import Partner
from datetime import datetime

class PartnersRepository(BaseRepository):
    def get_partners(self):
        return self.session.query(Partners).all()

    def create_partner(self, partner: Partner):
        partner_in_db = Partners(**partner.dict())
        self.session.add(partner_in_db)
        self.session.commit()
        self.session.refresh(partner_in_db)
        return partner_in_db

    def get_partner_by_id(self, id: int):
        return self.session.query(Partners).filter(Partners.id == id).first()

    def update_partner(self, id: int, partner: Partner):
        partner_in_db = self.session.query(Partners).filter(Partners.id == id).first()
        partner_in_db.name = partner.name
        partner_in_db.address = partner.address
        partner_in_db.category = partner.category
        partner_in_db.body = partner.body
        partner_in_db.date = partner.date
        self.session.commit()
        return partner_in_db

    def delete_partner(self, id: int):
        partner_in_db = self.session.query(Partners).filter(Partners.id == id).first()
        self.session.delete(partner_in_db)
        self.session.commit()
        return partner_in_db

    def get_partners_by_category(self, category: str):
        return self.session.query(Partners).filter(Partners.category == category).all()

    def update_date(self, id: int, date: datetime):
        partner_in_db = self.session.query(Partners).filter(Partners.id == id).first()
        partner_in_db.date = date
        self.session.commit()
        return partner_in_db

    def get_actual_partners(self):
        return self.session.query(Partners).filter(Partners.date >= datetime.now()).all()