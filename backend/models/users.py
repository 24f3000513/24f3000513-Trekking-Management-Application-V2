from models import db
from sqlalchemy import Enum
from extensions import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    hashed_password  = db.Column(db.String(255), nullable=False)
    role = db.Column(Enum('admin','staff','trekker',name='role'),nullable=False,default='trekker')
    address = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    is_blacklisted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    staff = db.relationship('Staff', backref='user', lazy=True)
    bookings = db.relationship('Bookings', backref='user', lazy=True)
    ratings = db.relationship('Ratings', backref='user', lazy=True)
    
    def set_password(self, password):
        self.hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.hashed_password, password)