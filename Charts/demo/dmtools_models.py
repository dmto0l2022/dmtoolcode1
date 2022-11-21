import datetime as dt
from flask import current_app as app
##from app import login_manager
login = app.login_manager
#from app import db
db = app.extensions['sqlalchemy'].db

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from sqlalchemy import CHAR, Column, DECIMAL, Enum, ForeignKey, text, DateTime, Date
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, LONGBLOB, MEDIUMTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
# flask_dance.consumer.storage.sqla
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage

Base = declarative_base()
metadata = Base.metadata

#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(user_id)

#@login_manager.load_user

## https://stackoverflow.com/questions/51209763/attributeerror-type-object-user-has-no-attribute-get

@login.user_loader
def load_user(user):
    return User.query.get(user) ## added .query.


class User(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)    
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=dt.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Post {}>'.format(self.body)    
    

class Experiment(Base):
    __tablename__ = 'experiments'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))


class LimitDisplay(Base):
    __tablename__ = 'limit_displays'

    id = Column(INTEGER(11), primary_key=True)
    limit_id = Column(INTEGER(11))
    plot_id = Column(INTEGER(11))
    color = Column(String(255), server_default=text("'k'"))
    style = Column(String(255), server_default=text("'line'"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class LimitOwnership(Base):
    __tablename__ = 'limit_ownerships'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(INTEGER(11))
    limit_id = Column(INTEGER(11))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)



class Limit(Base):
    __tablename__ = 'limits'

    id = Column(INTEGER(11), primary_key=True)
    spin_dependency = Column(String(255))
    result_type = Column(String(255), server_default=text("'Personal'"))
    measurement_type = Column(String(60))
    nomhash = Column(LONGBLOB)
    x_units = Column(String(255), server_default=text("'GeV'"))
    y_units = Column(String(255), server_default=text("'cm^2'"))
    x_rescale = Column(String(255), server_default=text("'1'"))
    y_rescale = Column(String(255), server_default=text("'1'"))
    default_color = Column(String(255), server_default=text("'Blk'"))
    default_style = Column(String(255), server_default=text("'Line'"))
    data_values = Column(MEDIUMTEXT)
    data_label = Column(String(255))
    file_name = Column(String(255))
    data_comment = Column(String(255))
    data_reference = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    creator_id = Column(INTEGER(11))
    experiment = Column(String(255))
    rating = Column(INTEGER(11), server_default=text("0"))
    date_of_announcement = Column(Date)
    public = Column(TINYINT(1), server_default=text("0"))
    official = Column(TINYINT(1), server_default=text("0"))
    date_official = Column(Date)
    greatest_hit = Column(TINYINT(1), server_default=text("0"))
    date_of_run_start = Column(Date)
    date_of_run_end = Column(Date)
    year = Column(INTEGER(11))
        
 
