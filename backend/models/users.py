from models import db
from flask_security import UserMixin
import uuid

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    password  = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean, default=True)
    is_blacklisted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    fs_uniquifier = db.Column(db.String(64),unique=True,nullable=False,default=lambda: str(uuid.uuid4()))
    
    staff = db.relationship('Staff', backref='user', lazy=True)
    bookings = db.relationship('Bookings', backref='user', lazy=True)
    ratings = db.relationship('Ratings', backref='user', lazy=True)
    role = db.relationship("Role", backref="users")
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=True)

    def __repr__(self):
        return f"<User {self.email}>"