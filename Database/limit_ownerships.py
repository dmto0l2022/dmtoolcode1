from sqlalchemy.dialects.mysql import LONGTEXT

from sqlalchemy import Column, String, Integer, Date, DateTime, LargeBinary

from base import Base

class cls_limit_ownerships(Base):
    __tablename__ = 'limit_ownerships'
    id=Column(Integer, primary_key=True)
    user_id = COLUMN(Integer)
    limit_id = COLUMN(Integer)
    created_at = COLUMN(DateTime)
    updated_at = COLUMN(DateTime)

 