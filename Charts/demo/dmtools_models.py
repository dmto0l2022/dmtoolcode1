import datetime as dt
from flask import current_app as app
##from app import login_manager
login = app.login_manager
#from app import db
db = app.extensions['sqlalchemy'].db

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from sqlalchemy import CHAR, Column, DECIMAL, Enum, ForeignKey, text, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
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
    
class Country(Base):
    __tablename__ = 'country'

    Code = Column(CHAR(3), primary_key=True, server_default=text("''"))
    Name = Column(CHAR(52), nullable=False, server_default=text("''"))
    Continent = Column(Enum('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America'), nullable=False, server_default=text("'Asia'"))
    Region = Column(CHAR(26), nullable=False, server_default=text("''"))
    SurfaceArea = Column(DECIMAL(10, 2), nullable=False, server_default=text("0.00"))
    IndepYear = Column(SMALLINT(6))
    Population = Column(INTEGER(11), nullable=False, server_default=text("0"))
    LifeExpectancy = Column(DECIMAL(3, 1))
    GNP = Column(DECIMAL(10, 2))
    GNPOld = Column(DECIMAL(10, 2))
    LocalName = Column(CHAR(45), nullable=False, server_default=text("''"))
    GovernmentForm = Column(CHAR(45), nullable=False, server_default=text("''"))
    HeadOfState = Column(CHAR(60))
    Capital = Column(INTEGER(11))
    Code2 = Column(CHAR(2), nullable=False, server_default=text("''"))


class Experiments(Base):
    
     __tablename__ = 'Experiments'
        
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiments'


class LimitDisplays(models.Model):
    limit_id = models.IntegerField(blank=True, null=True)
    plot_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit_displays'


class LimitOwnerships(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    limit_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limit_ownerships'


class Limits(models.Model):
    spin_dependency = models.CharField(max_length=255, blank=True, null=True)
    result_type = models.CharField(max_length=255, blank=True, null=True)
    measurement_type = models.CharField(max_length=60, blank=True, null=True)
    nomhash = models.TextField(blank=True, null=True)
    x_units = models.CharField(max_length=255, blank=True, null=True)
    y_units = models.CharField(max_length=255, blank=True, null=True)
    x_rescale = models.CharField(max_length=255, blank=True, null=True)
    y_rescale = models.CharField(max_length=255, blank=True, null=True)
    default_color = models.CharField(max_length=255, blank=True, null=True)
    default_style = models.CharField(max_length=255, blank=True, null=True)
    data_values = models.TextField(blank=True, null=True)
    data_label = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    data_comment = models.CharField(max_length=255, blank=True, null=True)
    data_reference = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    experiment = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    date_of_announcement = models.DateField(blank=True, null=True)
    public = models.IntegerField(blank=True, null=True)
    official = models.IntegerField(blank=True, null=True)
    date_official = models.DateField(blank=True, null=True)
    greatest_hit = models.IntegerField(blank=True, null=True)
    date_of_run_start = models.DateField(blank=True, null=True)
    date_of_run_end = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'limits'


class PlotOwnerships(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    plot_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plot_ownerships'


class Plots(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    x_min = models.CharField(max_length=255, blank=True, null=True)
    x_max = models.CharField(max_length=255, blank=True, null=True)
    y_min = models.CharField(max_length=255, blank=True, null=True)
    y_max = models.CharField(max_length=255, blank=True, null=True)
    x_units = models.CharField(max_length=255, blank=True, null=True)
    y_units = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    plot_png = models.TextField(blank=True, null=True)
    legend_png = models.TextField(blank=True, null=True)
    plot_eps = models.TextField(blank=True, null=True)
    legend_eps = models.TextField(blank=True, null=True)
    no_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plots'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class SimpleCaptchaData(models.Model):
    key = models.CharField(max_length=40, blank=True, null=True)
    value = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'simple_captcha_data'

