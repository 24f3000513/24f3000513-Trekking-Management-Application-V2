from functools import wraps
from flask import jsonify
from flask_security import auth_required, current_user


def role_required(required_role):
    def decorator(view_function):
        @auth_required("token")
        @wraps(view_function)
        def wrapper(*args, **kwargs):

            if not current_user.active:
                return jsonify({"message": "Account is inactive"}), 403

            if current_user.is_blacklisted:
                return jsonify({"message": "Account is blacklisted"}), 403

            if(current_user.role is None or current_user.role.name != required_role):
                return jsonify({"message": "Permission denied"}), 403

            return view_function(*args, **kwargs)
        return wrapper
    return decorator