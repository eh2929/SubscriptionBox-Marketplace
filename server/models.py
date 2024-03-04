from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy
from flask import validates

from config import db

# Models go here!

# User Model


class User(db.Model, SerializerMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String)
    total_active_orders = db.Column(db.Integer)

    # Relationships
    orders = db.relationship('Order', back_populates='user')
    # Serializers
    serialize_rules = ('-orders.user',)
    # Validation
    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError(f"{key}. Invalid email address.")
        else:
            return email


class Order(db.Model, SerializerMixin):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)

    # Foreign Key to User Model
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    subscription_id = db.Column(db.Integer, db.ForeignKey("subscription.id"))

    status = db.Column(db.String)
    frequency = db.Column(db.String)
    quantity = db.Column(db.Integer)
    total_monthly_price = db.Column(db.Float)

    # Relationships
    user = db.relationship('User', back_populates='orders')
    subscription = db.relationship('Subscription', back_populates='orders')
    # Serializers
    serialize_rules = ('-user.orders', '-subscription.orders',)
    # Validation
    @validates('quantity', 'frequency')
    def validate_not_empty(self, key, value):
        if not value:
            raise ValueError(f"{key} is required.")
        else:
            return value


class Subscription(db.Model, SerializerMixin):
    __tablename__ = "subscription"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    subtotal_price = db.Column(db.Float)

    # Relationships
    orders = db.relationship('Order', back_populates='subscription')
    box = db.relationship('Box', back_populates='subscription')
    # Serializers
    serialize_rules = ('-orders.subscription',)
    # Validation
    @validates('description')
    def validate_description(self, key, value):
        if not value:
            raise ValueError(f"{key} is required.")
        else:
            return value


class Box(db.Model, SerializerMixin):
    __tablename__ = "box"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    included_items = db.Column(db.String)

    # Foreign Key to Subscription Model
    subscription_id = db.Column(db.Integer, db.ForeignKey("subscription.id"))

    # Relationships
    subscription = db.relationship('Subscription', back_populates='box')
    # Serializers
    serialize_rules = ('-subscription.box')
    # Validation
    @validates('name', 'included_items')
    def validate_name(self, key, value):
        if not value:
            raise ValueError(f"{key} is required.")
        else:
            return value
