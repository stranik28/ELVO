from schemas.transactions import TransactionSchema
from models.transactions import Transactions
from repository.base import BaseRepository
from typing import List

class TransactionRepository(BaseRepository):
    def get_transactions(self):
        return self.session.query(Transactions).all()

    def get_transaction(self, id: int):
        return self.session.query(Transactions).filter_by(id=id).first()

    def create_transaction(self, transaction: TransactionSchema):
        transaction = Transactions(**transaction.dict())
        self.session.add(transaction)
        self.session.commit()
        return transaction

    def update_transaction(self, id: int, transaction: TransactionSchema):
        transaction = self.get_transaction(id)
        transaction.user_id = transaction.user_id
        transaction.company_id = transaction.company_id
        transaction.amount = transaction.amount
        transaction.body = transaction.body
        self.session.commit()
        return transaction

    def delete_transaction(self, id: int):
        transaction = self.get_transaction(id)
        self.session.delete(transaction)
        self.session.commit()
        return transaction