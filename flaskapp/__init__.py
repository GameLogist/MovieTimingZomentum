import atexit
import datetime
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from flaskapp.config import Config

app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)
db = SQLAlchemy(app)


from flaskapp.scheduler import expired_ticket_removal_job
db.create_all()
from flaskapp import routes

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(expired_ticket_removal_job, trigger='interval', seconds=30)
scheduler.start()

atexit.register(lambda: scheduler.shutdown(wait=False))

