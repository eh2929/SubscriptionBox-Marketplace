#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Api, Resource
# Local imports
from config import app, db, api
from models import User, Order, Subscription, Box
# Initialize Api
api = Api(app)

# Views go here!
# Routes
@app.route('/')
def index():
    return '<h1>Project Server</h1><p>Change the endpoint to see data.</p>'

# '/subscriptions' route
class Subscriptions(Resource):
    def get(self):
        subs = [sub.to_dict() for sub in Subscription.query.all()]
        response = make_response(
            subs,
            200
        )
        return response

    def post(self):
        try:
            form_data = request.get_json()
            new_subscription = Subscription(
                description = form_data['description'],
                subtotal_price = form_data['subtotal_price']
            )
            db.session.add(new_subscription)
            db.session.commit()
            new_subscription_dict = new_subscription.to_dict()
            response = make_response(
                new_subscription_dict,
                201
            )
        except:
            response = make_response(
                {'error': 'Could not create subscription'},
                400
            )
        return response

api.add_resource(Subscriptions, '/subscriptions')

# '/subscription/<int:id>' route
class SubscriptionByID(Resource):
    def get(self, id):
        subscription = Subscription.query.filter_by(id=id).first()
        sub_dict = subscription.to_dictt()
        response = make_response(
            sub_dict,
            200
        )
        return response

    def patch(self, id):
        try:
            form_data = request.get_json()
            subscription = Subscription.query.filter_by(id=id).first()
            for attr in form_data:
                setattr(subscription, attr, form_data[attr])
            db.session.commit()
            subscription_dict = subscription.to_dict()
            response = make_response(
                subscription_dict,
                200
            )
        except:
            response = make_response(
                {'error': 'Could not update subscription'},
                400
            )
        return response
    
    # def delete(self, id):
api.add_resource(SubscriptionByID, '/subscriptions/<int:id>')

# '/boxes' route
class Boxes(Resource):
    def get(self):
        boxes = [box.to_dict() for box in Box.query.all()]
        response = make_response(
            boxes,
            200
        )
        return response
    
    def post(self):
        try:
            form_data = request.get_json()
            new_box = Box(
                name = form_data['name'],
                included_items = form_data['included_items'],
                subscription_id = form_data['subscription_id']
            )
            db.session.add(new_box)
            db.session.commit()
            new_box_dict = new_box.to_dict()
            response = make_response(
                new_box_dict,
                201
            )
        except:
            response = make_response(
                {'error': 'Could not create box'},
                400
            )
        return response
# '/boxes/<int:id>' route
class BoxByID(Resource):
    def get(self, id):
        box = Box.query.filter_by(id=id).first()
        box_dict = box.to_dict()
        response = make_response(
            box_dict,
            200
        )
        return response

    def patch(self, id):
        try:
            form_data = request.get_json()
            box = Box.query.filter_by(id=id).first()
            for attr in form_data:
                setattr(box, attr, form_data[attr])
            db.session.commit()
            box_dict = box.to_dict()
            response = make_response(
                box_dict,
                200
            )
        except:
            response = make_response(
                {'error': 'Could not update box'},
                400
            )
        return response




if __name__ == '__main__':
    app.run(port=5555, debug=True)

