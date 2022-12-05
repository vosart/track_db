from db import db_session
from models import User

user = User(name='Frosya Burlakova', salary=15000, email='fburlak_top@gmail.com')
db_session.add(user)
db_session.commit()