from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

# User Model


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    total_active_orders = db.Column(db.Integer)

    # Relationships

    # Serializers

    # Validation


class Order(db.Model):
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

    # Serializers

    # Validation


class Subscription(db.Model):
    __tablename__ = "subscription"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    subtotal_price = db.Column(db.Float)

    # Relationships

    # Serializers

    # Validation


class Box(db.Model):
    __tablename__ = "box"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    included_items = db.Column(db.String)

    # Foreign Key to Subscription Model
    subscription_id = db.Column(db.Integer, db.ForeignKey("subscription.id"))

    # Relationships

    # Serializers

    # Validation
    #oh look a change
