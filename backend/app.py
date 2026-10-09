from flask import Config, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

def create_db():
    with app.app_context():
        db.create_all()
        print("Database created successfully.")
        existing_admin = User.query.filter_by(email=Config.ADMIN_EMAIL).first()
        if not existing_admin:
            admin = User( name='Admin',phone=Config.ADMIN_PHNO,email=Config.ADMIN_EMAIL,role='admin')
            admin.set_password(Config.ADMIN_PASSWORD)
            db.session.add(admin)
            db.session.commit()
            print("Default admin created successfully.")
        else: 
            print("Admin already exists.")
create_db()

@app.route('/')
def home():
    return jsonify({"message": "MAD2 Project: Database initiated successfully"})

if __name__ == '__main__':
    app.run(debug=True)