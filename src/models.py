from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base, engine


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    roles = relationship("RoleModel")


class RoleModel(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("users.id"))


Base.prepare(engine)
