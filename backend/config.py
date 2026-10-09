import os
class Config:
    APP_Name = "Treklet"
    
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///trekking.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    ADMIN_EMAIL = "admin@sherpabuddy.com"
    ADMIN_PHNO = "8897877707"
    ADMIN_PASSWORD = "mad2project24f"