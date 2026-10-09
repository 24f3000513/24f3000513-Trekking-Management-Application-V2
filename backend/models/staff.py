from models import db
from sqlalchemy import Enum

class Staff(db.Model):
    __tablename__ = 'staff'
    
    staff_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
    experience = db.Column(db.Integer, nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    status = db.Column(Enum('active','on holiday','suspended','left',name='staff_status'),nullable=False,default='active')
    emergency_contact = db.Column(db.String(15), nullable=False)
    verification_id = db.Column(db.String(100), nullable=False)
    joining_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    trek_slot = db.relationship('Trek_Slot', backref='assigned_staff', lazy=True)