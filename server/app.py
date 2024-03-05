#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import User, Order, Subscription, Box

# Local imports
from config import app, db, api

# Initialize Api
api = Api(app)


# Views go here!
@app.route("/")
def index():
    return "<h1>Project Server</h1><p>Change the endpoint to see data.</p>"


# User class
class Users(Resource):

    def get(self):
        users = [user.to_dict(rules=("-orders",)) for user in User.query.all()]
        return make_response(users, 200)

    def post(self):
        req_data = request.get_json()
        try:
            new_user = User(**req_data)

        except ValueError as e:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(new_user)
        db.session.commit()
        return make_response(new_user.to_dict(), 201)


api.add_resource(Users, "/users")


# User by ID class
class UserById(Resource):

    def get(self, id):
        user = User.query.get_or_404(id, description="User not found")
        return make_response(user.to_dict(rules=("-orders",)), 200)

    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return make_response({"errors": ["User not found"]}, 404)
        db.session.delete(user)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        user = User.query.filter(User.id == id).first()
        req_data = request.get_json()
        if not user:
            return make_response({"error": ["User not found"]}, 404)
        try:
            for key, value in req_data.items():
                setattr(user, key, value)
        except:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.commit()
        return make_response(user.to_dict(), 200)


api.add_resource(UserById, "/users/<int:id>")


# Order class
class Orders(Resource):

    def get(self):
        orders = [
            order.to_dict(rules=("-subscriptions",)) for order in Order.query.all()
        ]
        return make_response(orders, 200)

    def post(self):
        req_data = request.get_json()
        try:
            new_order = Order(
                subscription_id=req_data["subscription_id"],
                quantity=req_data["quantity"],
                frequency=req_data["frequency"],
            )
        except:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(new_order)
        db.session.commit()
        return make_response(new_order.to_dict(), 201)


api.add_resource(Orders, "/orders")


# Order by ID class
class OrderById(Resource):

    def get(self, id):
        order = Order.query.get_or_404(id, description="Order not found")
        return make_response(order.to_dict(), 200)

    def delete(self, id):
        order = Order.query.filter(Order.id == id).first()
        if not order:
            return make_response({"errors": ["Order not found"]}, 404)
        db.session.delete(order)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        order = Order.query.filter(Order.id == id).first()
        req_data = request.get_json()
        if not order:
            return make_response({"error": ["Order not found"]}, 404)
        try:
            for key, value in req_data.items():
                setattr(order, key, value)
        except:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.commit()
        return make_response(order.to_dict(), 200)


api.add_resource(OrderById, "/orders/<int:id>")


# '/subscriptions' route
class Subscriptions(Resource):
    def get(self):
        subs = [sub.to_dict() for sub in Subscription.query.all()]
        response = make_response(subs, 200)
        return response

    def post(self):
        try:
            form_data = request.get_json()
            new_subscription = Subscription(
                description=form_data["description"],
                subtotal_price=form_data["subtotal_price"],
            )
            db.session.add(new_subscription)
            db.session.commit()
            new_subscription_dict = new_subscription.to_dict()
            response = make_response(new_subscription_dict, 201)
        except:
            response = make_response({"error": "Could not create subscription"}, 400)
        return response


api.add_resource(Subscriptions, "/subscriptions")


# '/subscription/<int:id>' route
class SubscriptionByID(Resource):
    def get(self, id):
        subscription = Subscription.query.filter_by(id=id).first()
        sub_dict = subscription.to_dictt()
        response = make_response(sub_dict, 200)
        return response

    def patch(self, id):
        try:
            form_data = request.get_json()
            subscription = Subscription.query.filter_by(id=id).first()
            for attr in form_data:
                setattr(subscription, attr, form_data[attr])
            db.session.commit()
            subscription_dict = subscription.to_dict()
            response = make_response(subscription_dict, 200)
        except:
            response = make_response({"error": "Could not update subscription"}, 400)
        return response


api.add_resource(SubscriptionByID, "/subscriptions/<int:id>")


# '/boxes' route
class Boxes(Resource):
    def get(self):
        boxes = [box.to_dict() for box in Box.query.all()]
        response = make_response(boxes, 200)
        return response

    def post(self):
        try:
            form_data = request.get_json()
            new_box = Box(
                name=form_data["name"],
                included_items=form_data["included_items"],
                subscription_id=form_data["subscription_id"],
            )
            db.session.add(new_box)
            db.session.commit()
            new_box_dict = new_box.to_dict()
            response = make_response(new_box_dict, 201)
        except:
            response = make_response({"error": "Could not create box"}, 400)
        return response


api.add_resource(Boxes, "/boxes")


# '/boxes/<int:id>' route
class BoxByID(Resource):
    def get(self, id):
        box = Box.query.filter_by(id=id).first()
        box_dict = box.to_dict()
        response = make_response(box_dict, 200)
        return response

    def patch(self, id):
        try:
            form_data = request.get_json()
            box = Box.query.filter_by(id=id).first()
            for attr in form_data:
                setattr(box, attr, form_data[attr])
            db.session.commit()
            box_dict = box.to_dict()
            response = make_response(box_dict, 200)
        except:
            response = make_response({"error": "Could not update box"}, 400)
        return response


api.add_resource(BoxByID, "/boxes/<int:id>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
