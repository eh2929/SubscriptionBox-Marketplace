#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, make_response, request, session
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import User, Order, Subscription, Box

# Local imports
from config import app, db, api

# Secret Key
app.secret_key = b"\x91\xd8\xcb.\xf6L\xa8;}Ll\xae[\t\xa0\x1d"
# To genereate the secret key in the terminal run `python -c 'import os; print(os.urandom(16))'`
# Hexadecimal string representation

# Api.error_router = lambda self, handler, e: handler(e) --> error handling option
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
        session["user_id"] = new_user.id
        return make_response(new_user.to_dict(), 201)

# The second route is non-RESTful and allows users who are signing up to post a User.
api.add_resource(Users, "/users", '/signup')


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
        order = Order.query.filter_by(id=id).first()
        if not order:
            return make_response({"errors": ["Order not found"]}, 404)
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
        subs = [
            sub.to_dict(rules=("-boxes", "-orders")) for sub in Subscription.query.all()
        ]
        if not subs:
            response = make_response({"error": "No subscriptions found"}, 404)
        else:
            response = make_response(subs, 200)
        return response

    def post(self):
        try:
            form_data = request.get_json()
            new_subscription = Subscription(
                description=form_data["description"],
                price_per_box=form_data["price_per_box"],
            )
            db.session.add(new_subscription)
            db.session.commit()
            new_subscription_dict = new_subscription.to_dict(rules=("-box", "-orders"))
            response = make_response(new_subscription_dict, 201)
        except:
            response = make_response({"error": "Could not create subscription"}, 400)
        return response


api.add_resource(Subscriptions, "/subscriptions")


# '/subscription/<int:id>' route
class SubscriptionByID(Resource):

    def get(self, id):
        subscription = Subscription.query.filter_by(id=id).first()
        if not subscription:
            return make_response({"error": "Subscription not found"}, 404)
        subscription_dict = subscription.to_dict(
            "-box",
            "-orders",
        )
        response = make_response(subscription_dict, 200)
        return response

    def patch(self, id):
        try:
            form_data = request.get_json()
            subscription = Subscription.query.filter_by(id=id).first()
            if not subscription:
                return make_response({"error": "Subscription not found"}, 404)
            for attr in form_data:
                setattr(subscription, attr, form_data[attr])
            db.session.commit()
            subscription_dict = subscription.to_dict(
                rules=(
                    "-box",
                    "-orders",
                )
            )
            response = make_response(subscription_dict, 200)
        except:
            response = make_response({"error": "Could not update subscription"}, 400)
        return response

    def delete(self, id):
        subs = Subscription.query.filter_by(id=id).first()
        if not subs:
            return make_response({"error": "Subscription not found"}, 404)
        db.session.delete(subs)
        db.session.commit()
        return make_response({}, 204)


api.add_resource(SubscriptionByID, "/subscriptions/<int:id>")


# '/boxes' route
class Boxes(Resource):

    def get(self):
        boxes = [box.to_dict(rules=("-subscription",)) for box in Box.query.all()]
        response = make_response(boxes, 200)
        return response

    def post(self):
        try:
            form_data = request.get_json()
            if (
                "name" not in form_data
                or "included_items" not in form_data
                or "image_url" not in form_data
            ):
                return make_response({"error": "Missing required field"}, 400)
            new_box = Box(
                name=form_data["name"],
                included_items=form_data["included_items"],
                image_url=form_data["image_url"],
                subscription_id=form_data.get(
                    "subscription_id", None
                ),  # use .get() method to make subscription_id optional
            )
            db.session.add(new_box)
            db.session.commit()
            new_box_dict = new_box.to_dict(rules=("-subscription",))
            response = make_response(new_box_dict, 201)
        except:
            response = make_response({"error": "Could not create box"}, 400)
        return response


api.add_resource(Boxes, "/boxes")


# '/boxes/<int:id>' route
class BoxByID(Resource):

    def get(self, id):
        box = Box.query.filter_by(id=id).first()
        box_dict = box.to_dict(rules=("-subscription",))
        if not box:
            response = make_response({"error": "Box not found"}, 404)
        response = make_response(box_dict, 200)
        return response

    def patch(self, id):
        try:
            form_data = request.get_json()
            box = Box.query.filter_by(id=id).first()
            if not box:
                return make_response({"error": "Box not found"}, 404)
            for attr in form_data:
                setattr(box, attr, form_data[attr])
            db.session.commit()
            box_dict = box.to_dict(rules=("-subscription",))
            response = make_response(box_dict, 200)
        except:
            response = make_response({"error": "Could not update box"}, 400)
        return response

    def delete(self, id):
        boxes = Box.query.filter_by(id=id).first()
        if not boxes:
            return make_response({"errors": "Box not found"}, 404)
        db.session.delete(boxes)
        db.session.commit()
        return make_response({}, 204)


api.add_resource(BoxByID, "/boxes/<int:id>")

class Login(Resource):
    def post(self):
        try:
            form_data = request.get_json()
            user = User.query.filter_by(username=form_data["username"]).first()
            if not user:
                response = make_response({"error": "Username not found"}, 404)
            else:
                session["user_id"] = user.id
                response = make_response(user.to_dict(), 200)
        except:
            response = make_response({"error": "Could not login"}, 400)
        return response

api.add_resource(Login, "/login")

class CheckSession(Resource):

    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if not user:
            response = make_response({'error': 'Invalid username or password'}, 401) 
        elif user:
            return user.to_dict()
        else:
            response = make_response({'error': 'Login failed'}, 401)
            return response

api.add_resource(CheckSession, '/check_session')

if __name__ == "__main__":
    app.run(port=5555, debug=True)
