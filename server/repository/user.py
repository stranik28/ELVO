from models.users import users
from models.qr_codes import QrCodes
from schemas.user import UserBaseSchema
from repository.base import BaseRepository
from fastapi import HTTPException

from Crypto.Cipher import DES 

from database.connections import get_database_connection

def generate_qr_code(id: int) -> str:
    # зашифровать id в строку и записать в переменную
    # вернуть строку
    def pad(text):
        while len(text) % 8 != 0:
            text += b' '
        return text
    key = b'keykey12'
    des = DES.new(key, DES.MODE_ECB)
    # id to bytes
    id = id.to_bytes(8, byteorder='big')
    padded_text = pad(id)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

def get_qr_code_id(qr_code: str) -> int:
    # расшифровать строку в id и записать в переменную
    # вернуть id
    def pad(text):
        while len(text) % 8 != 0:
            text += b' '
        return text
    key = b'keykey12'
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(qr_code)
    decrypted_text = des.decrypt(padded_text)
    return int.from_bytes(decrypted_text, byteorder='big')


class UserRepository(BaseRepository):
    def get_all(self):
        return self.session.query(users).all()

    def get_user_by_id(self, id: int):
        user = self.session.query(users).filter(users.id == id).first()
        if(not user):
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def get_user_by_login(self, login: str):
        user = self.session.query(users).filter(users.login == login).first()
        return user

    def create_user(self, user: UserBaseSchema):
        # exlude unset fields
        user = user.dict(exclude_unset=True)
        if(self.get_user_by_login(user["login"])):
            raise HTTPException(status_code=400, detail="User already exists")
        # create user
        user = users(**user)
        # add user to session
        self.session.add(user)
        # commit session
        self.session.commit()
        # return user id
        return user.id
    
    def update_user(self, id: int, user: UserBaseSchema):
        # exlude unset fields
        userDict = user.dict(exclude_unset=True)
        # get user
        user = self.get_user_by_id(id)
        if(not user):
            raise HTTPException(status_code=404, detail="User not found")
        # update user
        for key, value in userDict.items():
            setattr(user, key, value)
        # commit session
        self.session.commit()
        # return user id
        return user.id
    
    def delete_user(self, id: int):
        # get user
        user = self.get_user_by_id(id)
        if(not user):
            raise HTTPException(status_code=404, detail="User not found")
        # delete user
        self.session.delete(user)
        # commit session
        self.session.commit()
        # return user id
        return user.id
    
    def patch_user(self, id: int, user: UserBaseSchema):
        # exlude unset fields
        userDict = user.dict(exclude_unset=True)
        # get user
        user = self.get_user_by_id(id)
        if(not user):
            raise HTTPException(status_code=404, detail="User not found")
        # update user
        for key, value in userDict.items():
            if(value):
                setattr(user, key, value)
        # commit session
        self.session.commit()
        # return user id
        return user.id
    

    # сделай ендпоинт под генерацию qr кода
    def generate_qr_code(self, id: int):
        # get user
        user = self.get_user_by_id(id)
        if(not user):
            raise HTTPException(status_code=404, detail="User not found")
        # generate qr code
        qr_code = generate_qr_code(id)
        # add qr code to session
        # create new qr code model
        qr_code = QrCodes(hash=qr_code)
        #change qr_code_id in user
        user.qr_id = qr_code.id
        # add qr code to session
        self.session.add(qr_code)