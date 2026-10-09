from models import db
from sqlalchemy import Enum

class Bookings(db.Model):
    __tablename__ = 'bookings'

    booking_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('trek_slot.slot_id'), nullable=False)
    booking_status = db.Column(Enum('Booked','Completed','Cancelled','Refunded','Refund-Cancelled',name='booking_status'),nullable=False,default='Booked')
    booking_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())    
    no_of_people = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    is_cancelled = db.Column(db.Boolean, nullable=False, default=False)
    refund_status = db.Column(Enum('Not-Initiated','Pending','Cancelled','Refunded',name='refund_status'),nullable=False,default='Not-Initiated')
    refund_amount = db.Column(db.Float, nullable=True)
    cancellation_date = db.Column(db.DateTime, nullable=True)
    cancellation_reason = db.Column(db.String(255), nullable=True)