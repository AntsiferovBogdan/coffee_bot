from datetime import datetime

from db import Base, engine
from sqlalchemy import Column, DateTime, Integer, String, BigInteger, ForeignKey


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(256))
    telegram_id = Column(BigInteger, unique=True, nullable=False, index=True)
    phone_number = Column(String)


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    status = Column(String, nullable=False, default='open')
    created_at = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f'Заказ {self.id} от {self.created_at.strftime("%d %B %Y")}, статус - {self.status}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
