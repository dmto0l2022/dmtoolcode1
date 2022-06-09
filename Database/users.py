##-- RubyDB.users definition

#--limit_id = Column(Integer)
#--plot_id = Column(Integer)
#--color  = Column(String(255))
#--style  = Column(String(255))
#--created_at = Column(DateTime)
#--updated_at = Column(DateTime)

class cls_users(Base):
  __tablename__ = 'users'
  id=Column(Integer, primary_key=True)
  login = Column(String(255))
  email = Column(String(255))
  crypted_password = (String(40))
  salt = (String(40))
  created_at = Column(DateTime)
  updated_at = Column(DateTime) 
  remember_token= Column(String(255)),
  remember_token_expires_at = Column(DateTime)
  reset_password_code = (String(255))
  reset_password_code_until = Column(DateTime)
  activation_code = (String(255))
  activated_at = Column(DateTime)
