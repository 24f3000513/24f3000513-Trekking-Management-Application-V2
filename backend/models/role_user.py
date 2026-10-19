from models import db

class RoleUser(db.Model):
    __tablename__ = "role_user"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.user_id"),nullable=False)
    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"),nullable=False)

    __table_args__ = (
        db.UniqueConstraint("user_id","role_id",name="unique_user_role"),
    )

    def __repr__(self):
        return (f"<RoleUser user_id={self.user_id} "f"role_id={self.role_id}>")