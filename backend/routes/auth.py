from flask import Blueprint, request, jsonify
from flask_security import auth_required, hash_password
from models import db, User, Role
from sqlalchemy import or_
from flask_security import verify_and_update_password, current_user
import uuid

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    identifier = data.get("identifier", "").strip()
    password = data.get("password", "")
    if not identifier or not password:
        return jsonify({"message": "Email/phone and password are required"}), 400

    user = User.query.filter(or_(User.email == identifier.lower(),User.phone == identifier)).first()
    if(user is None or not user.active or user.is_blacklisted):
        return jsonify({"message": "Invalid email/phone or password"}), 401
    if not verify_and_update_password(password, user):
        return jsonify({"message": "Invalid email/phone or password"}), 401
    token = user.get_auth_token()
    
    return jsonify({
        "message": "Login successful",
        "authentication_token": token,
        "user": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role.name
        }}), 200

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "").strip().lower()
    email = data.get("email", "").strip().lower()
    phone = data.get("phone", "").strip()
    password = data.get("password", "")
    cnf_password = data.get("cnf_password", "")
    address = data.get("address", "").strip()
    
    if not name or not email or not phone or not password or not cnf_password or not address:
        return jsonify({"message": "All fields are required"}), 400

    if password != cnf_password:
        return jsonify({"message": "Passwords do not match"}), 400

    if User.query.filter(or_(User.email == email, User.phone == phone)).first():
        return jsonify({"message": "Email or phone already exists"}), 400
    
    trekker = Role.query.filter_by(name="trekker").first()
    if trekker is None:
        return jsonify({"message": "Registration is temporarily unavailable"}), 500

    new_user = User(name=name,email=email,phone=phone,password=hash_password(password),address=address,active=True,roles=[trekker])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        "message": "User registered successfully",
        "user": {
            "user_id": new_user.user_id,
            "name": new_user.name,
            "email": new_user.email,
            "phone": new_user.phone,
            "address": new_user.address,
            "role": trekker
        }}), 201

@auth_bp.route("/logout", methods=["POST"])
@auth_required("token")
def logout():
    current_user.fs_uniquifier = str(uuid.uuid4())
    db.session.commit()
    return jsonify({"message": "Logout successful"}), 200
