import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'database', 'books.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]