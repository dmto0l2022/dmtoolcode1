from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Address(Base):
     __tablename__ = "address"

     id = Column(Integer, primary_key=True)
     email_address = Column(String, nullable=False)
     user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

     user = relationship("User", back_populates="addresses")

     def __repr__(self):
         return f"Address(id={self.id!r}, email_address={self.email_address!r})"