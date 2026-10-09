from models import db

class Ratings(db.Model):
    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    trek_id = db.Column(db.Integer, db.ForeignKey('trek_info.trek_id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('trek_slot.slot_id'), nullable=False)
    rating_value = db.Column(db.Float, nullable=False)
    service_rating = db.Column(db.Float, nullable=True)
    review_text = db.Column(db.String(255), nullable=True)
    submitted_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    __table_args__ = (
        db.UniqueConstraint('user_id','slot_id',name='unique_user_slot_rating'),
        db.CheckConstraint('rating_value >= 1 AND rating_value <= 5',name='check_rating_value'),
        db.CheckConstraint('service_rating IS NULL OR ''(service_rating >= 1 AND service_rating <= 5)', name='check_service_rating'),
    )