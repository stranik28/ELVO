from pydantic import BaseModel

class Company(BaseModel):
    name: str
    description: str

class CompanyInDB(Company):
    id: int