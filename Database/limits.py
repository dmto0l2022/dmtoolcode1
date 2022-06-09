from sqlalchemy.dialects.mysql import LONGTEXT

from sqlalchemy import Column, String, Integer, Date, DateTime, LargeBinary

from base import Base

class cls_limits(Base):
    __tablename__ = 'limits'
    id=Column(Integer, primary_key=True)
    spin_dependency = Column(String(255))
    result_type = Column(String(255))
    measurement_type = Column(String(60))
    nomhash = Column(LargeBinary)
    x_units = Column(String(255))
    y_units = Column(String(255))
    x_rescale = Column(String(255))
    y_rescale = Column(String(255))
    default_color = Column(String(255))
    default_style = Column(String(255))
    data_values = Column(LONGTEXT)
    data_label = Column(String(255))
    file_name = Column(String(255))
    data_comment = Column(String(255))
    data_reference = Column(String(255))
    created_at = COLUMN(DateTime)
    updated_at = COLUMN(DateTime)
    creator_id = COLUMN(Integer)
    experiment = Column(String(255))
    rating = COLUMN(Integer)
    date_of_announcement = COLUMN(date)
    public = COLUMN(Integer)
    official = COLUMN(Integer)
    date_official = COLUMN(Date)
    greatest_hit = COLUMN(Integer)
    date_of_run_start = COLUMN(Date)
    date_of_run_end = COLUMN(Date)
    year = COLUMN(Integer)

    def __init__(self):
        self.spin_dependency = ''
        self.result_type = 'Personal'
        self.measurement_type = ''
        self.nomhash = '?'
        self.x_units = 'GeV'
        self.y_units = 'cm^2'
        self.x_rescale = '1'
        self.y_rescale = '1'
        self.default_color = 'Blk'
        self.default_style = 'Line'
        self.data_values = ''
        self.data_label = ''
        self.file_name = ''
        self.data_comment = ''
        self.data_reference = ''
        self.created_at = ''
        self.updated_at = ''
        self.creator_id = '0'
        self.experiment = ''
        self.rating = '0'
        self.date_of_announcement = ''
        self.public = '0'
        self.official = ''
        self.date_official = '0'
        self.greatest_hit = '0'
        self.date_of_run_start = ''
        self.date_of_run_end = ''
        self.year = '0'
