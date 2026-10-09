from models import db
from sqlalchemy import Enum

class Trek_Info(db.Model):
    __tablename__ = 'trek_info'

    trek_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(Enum('Easy','Moderate','Hard','Extreme',name='trek_difficulty'),nullable=False)
    description = db.Column(db.Text, nullable=True)
    elevation_gain = db.Column(db.Integer, nullable=False)
    est_time = db.Column(db.String(50), nullable=False)
    schedule = db.Column(db.Text, nullable=False)
    pickup_point = db.Column(db.String(100), nullable=False)
    drop_point = db.Column(db.String(100), nullable=False)
    route_style = db.Column(Enum('Loop','In-and-Out','One Way','Lollipop',name='route_style'),nullable=False)
    activity_status = db.Column(Enum('Open','Seasonally Closed','Permanently Closed','Blacklisted','Deleted',name='trek_activity_status'),nullable=False,default='Open')
    is_blacklisted = db.Column(db.Boolean, nullable=False, default=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    trek_slot = db.relationship('Trek_Slot',backref = 'trek_info',lazy = True)
    images = db.relationship('Images', backref='trek_info', lazy=True)
    ratings = db.relationship('Ratings', backref='trek_info', lazy=True)
    features = db.relationship('Trek_Features', backref='trek_info', lazy=True)