from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, User, Role
from flask_security import Security, SQLAlchemyUserDatastore, hash_password, auth_required, current_user
from routes.auth import auth_bp
from extensions import user_datastore

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
security = Security(app, user_datastore)

app.register_blueprint(auth_bp)

def create_db():
    with app.app_context():
        db.create_all()
        print("Database created successfully.")
        admin = user_datastore.find_or_create_role(name='admin', description='Admin role')
        staff = user_datastore.find_or_create_role(name='staff', description='Staff role')
        trekker = user_datastore.find_or_create_role(name='trekker', description='Trekker role')
        existing_admin = user_datastore.find_user(email=Config.ADMIN_EMAIL)        
        if not existing_admin:
            admin_user = User(name="Admin",email=Config.ADMIN_EMAIL,
                        phone=Config.ADMIN_PHNO,password=hash_password(Config.ADMIN_PASSWORD),
                        active=True,role=admin)
            db.session.add(admin_user)            
            db.session.commit()
            print("Default admin created successfully.")
        else:
            print("Admin already exists.")
create_db()

@app.route('/')
def home():
    return jsonify({"message": "MAD2 Project: Auth and RBAC System working"})

@app.route("/api/me", methods=["GET"])
@auth_required("token")
def get_current_user():
    return jsonify({
        "user_id": current_user.user_id,
        "name": current_user.name,
        "email": current_user.email,
        "roles": [role.name for role in current_user.roles],
    })

if __name__ == '__main__':
    app.run(debug=True)