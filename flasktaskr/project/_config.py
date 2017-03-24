import os


# grab a folder where the script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = '19b71b0ff9850e74c9c90e09bb0b05121ef98675cc990f803069613ccb8b0604524375c30ec27e7bb3a03f0eff66ebe6'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH