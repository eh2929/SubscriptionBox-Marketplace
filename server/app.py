#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import User, Order, Subscription, Box

# Local imports
from config import app, db, api


# Views go here!

# User class


class Users(Resource):
    # test
    def get(self):
        users = [user.to_dict(rules=("-orders",)) for user in User.query.all()]
        return make_response(users, 200)

    # test
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
    # tested - working
    def get(self, id):
        user = User.query.get_or_404(id, description="User not found")
        return make_response(user.to_dict(rules=("-orders",)), 200)

    # test
    def delete(self, id):
        user = User.query.filter(User.id == id).first()
        if not user:
            return make_response({"errors": ["User not found"]}, 404)
        db.session.delete(user)
        db.commit()
        return make_response({}, 204)

    # test
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
    # test
    def get(self):
        orders = [order.to_dict() for order in Order.query.all()]
        return make_response(orders, 200)

    # test
    def post(self):
        req_data = request.get_json()
        try:
            new_order = Order(**req_data)
        except ValueError as e:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(new_order)
        db.session.commit()
        return make_response(new_order.to_dict(), 201)


api.add_resource(Orders, "/orders")


# Order by ID class
class OrderById(Resource):
    # test
    def get(self, id):
        order = Order.query.get_or_404(id, description="Order not found")
        return make_response(order.to_dict(), 200)

    # test
    def delete(self, id):
        order = Order.query.filter(Order.id == id).first()
        if not order:
            return make_response({"errors": ["Order not found"]}, 404)
        db.session.delete(order)
        db.commit()
        return make_response({}, 204)

    # test
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


@app.route("/")
def index():
    return "<h1>Project Server</h1><p>Change the endpoint to see data.</p>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
