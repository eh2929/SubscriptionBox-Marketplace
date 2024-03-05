from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from config import db

# from sqlalchemy.ext.associationproxy import association_proxy


# User Model
class User(db.Model, SerializerMixin):
    # Table
    __tablename__ = "user"
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    total_active_orders = db.Column(db.Integer)
    # Relationships
    orders = db.relationship("Order", back_populates="user", cascade="all,delete")
    # Serializers
    serialize_rules = ("-orders.user",)

    # Validation
    @validates("username")
    def validate_username(self, key, username):
        if not username:
            raise ValueError(f"{key} is required.")
        elif len(username) < 3:
            raise ValueError(f"{key}. Must be at least 3 characters long.")
        else:
            return username

    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError(f"{key}. Invalid email address.")
        elif not email:
            raise ValueError(f"{key} is required.")
        else:
            return email


# Order Model
class Order(db.Model, SerializerMixin):
    # Table
    __tablename__ = "order"
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    frequency = db.Column(db.String)
    quantity = db.Column(db.Integer)
    total_monthly_price = db.Column(db.Float)
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    subscription_id = db.Column(db.Integer, db.ForeignKey("subscription.id"))
    # Relationships
    user = db.relationship("User", back_populates="orders")
<<<<<<< HEAD
    subscription = db.relationship("Subscription", back_populates="orders")
=======
    subscription = db.relationship(
        "Subscription",
        back_populates="orders",
    )
>>>>>>> 684c45155977f75583faf97edfc3e53cf839f4a7
    # Serializers
    serialize_rules = (
        "-user.orders",
        "-subscription.orders",
    )

    # Predefined values
    VALID_STATUSES = ["pending", "shipped", "delivered", "cancelled"]
    VALID_FREQUENCIES = ["weekly", "biweekly", "monthly"]

    # Validation
    @validates("status")
    def validate_status(self, key, status):
        if not status:
            raise ValueError(f"{key} is required.")
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid {key}. Must be one of {self.VALID_STATUSES}.")
        return status

    @validates("frequency")
    def validate_frequency(self, key, frequency):
        if not frequency:
            raise ValueError(f"{key} is required.")
        if frequency not in self.VALID_FREQUENCIES:
            raise ValueError(f"Invalid {key}. Must be one of {self.VALID_FREQUENCIES}.")
        return frequency

    @validates("quantity")
    def validate_quantity(self, key, quantity):
        if not quantity:
            raise ValueError(f"{key} is required.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError(f"{key} must be a positive integer.")
        return quantity


# Subscription model
class Subscription(db.Model, SerializerMixin):
    # Table
    __tablename__ = "subscription"
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    subtotal_price = db.Column(db.Float)
    # Relationships
    orders = db.relationship(
        "Order", back_populates="subscription", cascade="all,delete"
    )
    box = db.relationship("Box", back_populates="subscription")
    # Serializers
    serialize_rules = ("-orders.subscription", "-box")

    # Validation
    @validates("description")
    def validate_description(self, key, value):
        if not value:
            raise ValueError(f"{key} is required.")
        else:
            return value
    @validates('subtotal_price')
    def validate_subtotal_price(self, key, value):
        if value <= -.01:
            raise ValueError(f"{key} is required.")
        else:
            return value


# Box model
class Box(db.Model, SerializerMixin):
    # Table
    __tablename__ = "box"
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    included_items = db.Column(db.String)
    # Foreign Key
    subscription_id = db.Column(db.Integer, db.ForeignKey("subscription.id"))
    # Relationships
    subscription = db.relationship(
        "Subscription", back_populates="box", cascade="all,delete"
    )
    # Serializers
    serialize_rules = ("-subscription.box",)

    # Validation
    @validates("name", "included_items")
    def validate_name(self, key, value):
        if not value:
            raise ValueError(f"{key} is required.")
        else:
            return value
