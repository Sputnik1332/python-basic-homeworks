"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, declared_attr, declarative_base, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
DB_ECHO = False


async_engine: AsyncEngine = create_async_engine(
    PG_CONN_URI,
    echo=DB_ECHO,
)


async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)

Session = async_session


class User(Base):
    name = Column(String, unique=False)
    username = Column(String, unique=True)
    email = Column(String)

    posts = relationship("Post", back_populates="user", uselist=True)

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, username={self.username!r}, email={self.email})"


class Post(Base):
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    title = Column(String)
    body = Column(Text, nullable=False, default="N/A")

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(user_id={self.user_id}, title={self.title!r}, body={self.body})"
