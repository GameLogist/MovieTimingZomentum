import os
import json
import unittest
from flaskapp import app, db

class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdatabase.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_booking(self):
        # Given
        payload = json.dumps({
            "user_name":"Ayush",
            "phone_number":"1234567890",
            "timing_start":630,
            "timing_end":930
        })

        # When
        response = self.app.post('/bookticket', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(int, type(response.json['id']))
        self.assertEqual(201, response.status_code)


    def test_edit_ticket_timing(self):
        # Given
        payload = json.dumps({
            "user_name":"Ayush",
            "phone_number":"1234567890",
            "timing_start":630,
            "timing_end":930
        })

        # When
        response = self.app.put('/bookticket', headers={"Content-Type": "application/json"}, data=payload)
        # t_id = response.json["id"]
        
        editticket_payload = json.dumps({
            "timing_start":930,
            "timing_end":1030
        })
        post_path = '/editticket/' + response.json['id']
        edit_response = self.app.post(post_path, headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()