import environ
import os

env = environ.Env()
environ.Env.read_env()

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

#LOG
LOG_FILE = env.str("LOG_FILE")

# URL DATA PATH
DATA_PHISHTANK = env.str('DATA_PHISHTANK')
DATA_OPENPHISH = env.str('DATA_OPENPHISH')

# Database
DATABASE_USER = env.str('DATABASE_USER')
DATABASE_PASSWORD = env.str('DATABASE_PASSWORD')
DATABASE_HOST = env.str('DATABASE_HOST')
DATABASE_PORT = env.str('DATABASE_PORT')
DATABASE_NAME = env.str('DATABASE_NAME')