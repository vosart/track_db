from db import db_session
from models import User

user = User(name='Aduma Takashi', salary=75000, email='adzuma_takashi@gmail.com')
db_session.add(user)
db_session.commit()