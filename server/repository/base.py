from abc import ABC, abstractmethod
from database.session import Session

class BaseRepository(ABC):
    def __init__(self, session: Session):
        self.session: Session = session