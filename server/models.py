from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

# from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

# User Model


class User(db.Model, SerializerMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    total_active_orders = db.Column(db.Integer)

    # Relationships
    orders = db.relationship("Order", back_populates="user")
    # Serializers
    serialize_rules = ("-orders.user",)

    # Validation
    @validates("username")
    def validate_username(self, key, username):
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        return username


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
    user = db.relationship("User", back_populates="orders")
    subscription = db.relationship("Subscription", back_populates="orders")
    # Serializers
    serialize_rules = (
        "-user.orders",
        "-subscription.orders",
    )
    # Validation


class Subscription(db.Model, SerializerMixin):
    __tablename__ = "subscription"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    subtotal_price = db.Column(db.Float)

    # Relationships
    orders = db.relationship("Order", back_populates="subscription")
    box = db.relationship("Box", back_populates="subscription")
    # Serializers

    serialize_rules = ("-orders.subscription",)


# Validation


class Box(db.Model, SerializerMixin):
    __tablename__ = "box"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    included_items = db.Column(db.String)

    # Foreign Key to Subscription Model
    subscription_id = db.Column(db.Integer, db.ForeignKey("subscription.id"))

    # Relationships
    subscription = db.relationship("Subscription", back_populates="box")
    # Serializers
    serialize_rules = ("-subscription.box",)


# Validation
# oh look a change
