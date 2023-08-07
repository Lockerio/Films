import os
import sqlalchemy as db


db_path = os.path.join('', 'Films.db')
engine = db.create_engine(f'sqlite:///{db_path}')
