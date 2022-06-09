
from sqlalchemy import Column, String, Integer, Date, DateTime

from base import Base


class cls_limit_displays(Base):
    __tablename__ = 'limit_displays'
    id=Column(Integer, primary_key=True)
    limit_id = Column(Integer)
    plot_id = Column(Integer)
    color  = Column(String(255))
    style  = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    

    def __init__(self):
        #self.title = title
        #self.release_date = release_date
        self.limit_id = NULL,
        self.plot_id = NULL,
        self.color = 'k',
        self.style = 'line',
        self.created_at = NULL,
        self.updated_at = NULL