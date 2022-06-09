from sqlalchemy import Column, String, Integer, Date, DateTime, LargeBinary

from base import Base

class cls_experiments(Base):
    __tablename__ = 'experiments'
    id=Column(Integer, primary_key=True)
    name=Column(String(255))
