from repository.base import BaseRepository
from sqlalchemy.orm import Session
from models import test

class TestRepository(BaseRepository):
    def get_test(self):
        # insert values into test table
        return self.session.query(test.Test).all()