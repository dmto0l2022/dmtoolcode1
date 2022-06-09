from sqlalchemy import Column, String, Integer, Date, DateTime, LargeBinary

from base import Base

class cls_plots(Base):
  __tablename__ = 'plots'
  id=Column(Integer, primary_key=True)
  name = Column(String(255)) DEFAULT NUL
  x_min = Column(String(255)) DEFAULT '1'
  x_max = Column(String(255)) DEFAULT '10000'
  y_min = Column(String(255)) DEFAULT '-54'
  y_max = Column(String(255)) DEFAULT '-26'
  x_units = Column(String(255)) DEFAULT 'GeV/c^2'
  y_units = Column(String(255)) DEFAULT 'cm2'
  user_id = Column(Integer)
  created_at = Column(DateTime)
  updated_at = Column(DateTime)
    Column(LargeBinary)
  plot_png = Column(LargeBinary)
  legend_png = Column(LargeBinary)
  plot_eps = Column(LargeBinary)
  legend_eps = Column(LargeBinary)
  no_id = Column(Integer)
 
  
  def __init__(self):
          self.x_min = '1'
          self.x_max = '10000'
          self.y_min = '-54'
          self.y_max = '-26'
          self.x_units = 'GeV/c^2'
          self.y_units = 'cm2'
          self.no_id ='0'