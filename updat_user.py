from db import db_session
from models import User

user = User.query.first()
user.salary = 250000
db_session.commit()