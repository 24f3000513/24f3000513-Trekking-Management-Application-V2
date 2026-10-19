class Config:
    APP_Name = "Treklet"
    
    SECRET_KEY = "koz7YPXhGewT15E3F0X79FrdAef6RmyN"
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///trekking.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = "dOJYwrnSlHKAJcG7mgMwA4B57iqZTvBk"
    
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    SECURITY_TOKEN_MAX_AGE = 600
    SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS = True

    ADMIN_EMAIL = "admin@treklet.com"
    ADMIN_PHNO = "8897877707"
    ADMIN_PASSWORD = "mad2project24f"