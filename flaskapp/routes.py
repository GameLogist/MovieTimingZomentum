import json
from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

from flaskapp import db
from flaskapp import api
from flaskapp.models import TicketModel

book_ticket_args = reqparse.RequestParser()
book_ticket_args.add_argument("user_name", type=str, help="User Name", required=True)
book_ticket_args.add_argument("phone_number", type=str, help="User's Phone Number", required=True)
book_ticket_args.add_argument("timing_start", type=int, help="Movie Start Time", required=True)
book_ticket_args.add_argument("timing_end", type=int, help="Movie End Time", required=True) 

edit_ticket_args = reqparse.RequestParser()
edit_ticket_args.add_argument("timing_start", type=int, help="Movie Start Time", required=True)
edit_ticket_args.add_argument("timing_end", type=int, help="Movie End Time", required=True)

view_ticket_args = reqparse.RequestParser()
view_ticket_args.add_argument("timing_start", type=int, help="Movie Start Time", required=True)
view_ticket_args.add_argument("timing_end", type=int, help="Movie End Time")

resource_fields = {
    'id':fields.Integer,
    'user_name':fields.String,
    'phone_number':fields.String,
    'timing_start':fields.Integer,
    'timing_end':fields.Integer,
    'state':fields.Integer
}

class BookTicket(Resource):
    @marshal_with(resource_fields)
    def post(self): # Book ticket
        args = book_ticket_args.parse_args()
        all_ticket = TicketModel.query.filter_by(timing_start=args['timing_start']).count()
        if all_ticket < 20 and args['timing_start'] < args['timing_end']:
            try:
                ticket = TicketModel(
                        user_name=args['user_name'], 
                        phone_number=args['phone_number'],
                        timing_start=args['timing_start'],
                        timing_end=args['timing_end'],
                        state=1
                        )
                db.session.add(ticket)
                db.session.commit()
                return ticket, 201
            except ValueError:
                error = "Phone number should be 10 digits"
                return json.dumps({ "error": error }), 200
        else:
            return '', 201

api.add_resource(BookTicket, "/bookticket")

class EditTicket(Resource):
    def put(self, ticket_id): # Update timing
        args = edit_ticket_args.parse_args()
        # db.session.query(TicketModel).filter(TicketModel.id==ticket_id).update({TicketModel.timing_start:args['timing_start'],TicketModel.timing_end:args['timing_end']})
        result = TicketModel.query.filter_by(id=ticket_id).first()
        result.timing_start=args['timing_start']
        result.timing_end=args['timing_end']
        db.session.commit()
        return '', 200

api.add_resource(EditTicket, "/editticket/<int:ticket_id>")

class ViewTickets(Resource):
    @marshal_with(resource_fields)
    def get(self):
        args = view_ticket_args.parse_args()
        result = TicketModel.query.filter_by(timing_start=args['timing_start']).all()
        return result

api.add_resource(ViewTickets, "/viewtickets")

class DeleteTicket(Resource):
    def delete(self, ticket_id): # Delete ticket
        ticket = TicketModel.query.filter_by(id=ticket_id).one()
        db.session.delete(ticket)
        db.session.commit()
        return '', 204

api.add_resource(DeleteTicket, "/deleteticket/<int:ticket_id>")

class ViewUser(Resource):
    @marshal_with(resource_fields)
    def get(self, ticket_id):
        result = TicketModel.query.filter_by(id=ticket_id).one()
        return result

api.add_resource(ViewUser, "/viewuser/<int:ticket_id>")
