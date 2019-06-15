from database import engine, db_session, Base
from models import User, Role

Base.metadata.create_all(bind=engine)

# Fill the tables with some data
user_1 = User(name='USER_1')
db_session.add(user_1)
user_2 = User(name='USER_2')
db_session.add(user_2)

role_1 = Role(name="ROLE_1", user_id=user_1)
db_session.add(role_1)
role_2 = Role(name="ROLE_2", user_id=user_2)
db_session.add(role_2)
db_session.commit()
