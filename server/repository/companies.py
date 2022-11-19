from models.companies import Companies
from repository.base import BaseRepository
from schemas.companies import CompanyInDB

class CompaniesRepository(BaseRepository):
    def get_companies(self):
        return self.session.query(Companies).all()

    def create_company(self, company: CompanyInDB):
        company_in_db = Companies(**company.dict())
        self.session.add(company_in_db)
        self.session.commit()
        self.session.refresh(company_in_db)
        return company_in_db

    def get_company_by_id(self, id: int):
        return self.session.query(Companies).filter(Companies.id == id).first()

    def update_company(self, id: int, company: CompanyInDB):
        company_in_db = self.session.query(Companies).filter(Companies.id == id).first()
        company_in_db.name = company.name
        company_in_db.description = company.description
        company_in_db.address = company.address
        company_in_db.phone = company.phone
        company_in_db.email = company.email
        self.session.commit()
        return company_in_db

    def delete_company(self, id: int):
        company_in_db = self.session.query(Companies).filter(Companies.id == id).first()
        self.session.delete(company_in_db)
        self.session.commit()
        return company_in_db