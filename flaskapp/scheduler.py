import atexit
from flaskapp import db
from flaskapp.models import TicketModel
from apscheduler.schedulers.background import BackgroundScheduler

def expired_ticket_removal_job():
    current_time = 1150
    expired_tickets = TicketModel.query.filter(current_time-TicketModel.timing_start >= 800).delete()
    db.session.commit()

