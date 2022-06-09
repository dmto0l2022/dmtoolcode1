from sqlalchemy import Column, String, Integer, Date, DateTime, LargeBinary

from base import Base

class cls_plot_ownerships(Base):
  __tablename__ = 'plot_ownerships'
  id=Column(Integer, primary_key=True)
  user_id = Column(Integer)
  plot_id = Column(Integer)
  created_at Column(DateTime)
  updated_at Column(DateTime)

  
  
  def __init__(self):
          self.user_id = '0'
          self.plot_id = '0'
          self.created_at = ''
          self.updated_at = ''
