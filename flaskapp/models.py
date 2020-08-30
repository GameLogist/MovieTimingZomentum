from flaskapp import db
from sqlalchemy.orm import validates

class TicketModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    timing_start = db.Column(db.Integer, nullable=False)
    timing_end = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Integer, nullable=False) # 1 -> Active | 0 -> Expired

    @validates('phone_number')
    def validate_phone_number(self, key, value):
        if len(value) != 10:
            raise ValueError(
                "Phone number should be 10 digits"
            )
        return value

    def __repr__(self):
        return f"Ticket(user_name = {user_name}, phone_number = {phone_number}, timings = {timing_start} to {timing_end}, state = {state})"
