import os

ADMIN_ID = 437585957
API_TOKEN = '1065687620:AAFB6lKF4cmUHX9B6AF5v0cjoLGf-WdAcDI'

basedir = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')
