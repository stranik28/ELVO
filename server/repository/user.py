from models.users import users
from models.qr_codes import QrCodes
from schemas.user import UserBaseSchema
from repository.base import BaseRepository
from fastapi import HTTPException
from passlib.hash import pbkdf2_sha256

from database.connections import get_database_connection

pwd_context = pbkdf2_sha256
pwd_context.using(salt="123".encode('utf-8'))

# реализовать хэш функцию 
def get_hash(id: int) -> str:
    return pwd_context.hash(str(id))


def generate_qr_code(id: int) -> str:
    # hash функция для хэширования айдишника
    return get_hash(id)


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
        if(user["password"]):
            user["hashed_password"] = pwd_context.hash(user["password"])
            user.pop("password")
        user = users(
            hashed_password=user["hashed_password"],
            login=user["login"],
            fio=user["fio"],
            email=user["email"],
            cars=[0]
        )
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
        hash = generate_qr_code(id)
        # get qr code by qr_id from user
        qr_code_from_db = self.session.query(QrCodes).filter(QrCodes.id == user.qr_id).first()
        # print(qr_code_from_db.__dict__)
        # if qr code exists
        if(qr_code_from_db):
            # update qr code
            qr_code_from_db.hash = hash
        else:
            # create qr code
            qr_code = QrCodes(hash=hash)
            # add qr code to session
            self.session.add(qr_code)
            # commit session
            self.session.commit()
            # update qr_id in user
            user.qr_id = qr_code.id
        # commit session
        self.session.commit()
        # return qr code
        return hash

    
    def get_qr_code(self, qr_code: str):
        # get qr code
        qr_code = self.session.query(QrCodes).filter(QrCodes.hash == qr_code).first()
        if(not qr_code):
            raise HTTPException(status_code=404, detail="QR code not found")
        print(qr_code.__dict__)
        user = self.session.query(users).filter(users.qr_id == qr_code.id).first()
        if(not user):
            raise HTTPException(status_code=401, detail="Not authorized")
        self.generate_qr_code(user.id)
        return "ok"