from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
    User model
"""
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String, nullable=False)





