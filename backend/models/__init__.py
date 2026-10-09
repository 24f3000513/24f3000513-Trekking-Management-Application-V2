from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .users import User
from .staff import Staff
from .trek_info import Trek_Info
from .trek_slot import Trek_Slot
from .trek_featuers import Trek_Features
from .bookings import Bookings
from .images import Images
from .ratings import Ratings
