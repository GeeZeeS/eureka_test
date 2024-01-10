import os


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://" \
                              f"{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:" \
                              f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

    MACHINE_URI = "http://machine:5001"


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


