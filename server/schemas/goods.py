from pydantic import BaseModel

class Good(BaseModel):
    name: str
    description: str
    cost: int
    company_id: int