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
    address = db.Column(db.String)
    admin = db.Column(db.Boolean, default=False)
    full_name = db.Column(db.String)
    phone_number = db.Column(db.String)
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

    @validates("address")  # new
    def validate_address(self, key, address):
        if not address:
            raise ValueError(f"{key} is required.")
        else:
            return address

    @validates("phone_number")
    def validate_phone_number(self, key, phone_number):
        if not phone_number:
            raise ValueError(f"{key} is required.")
        else:
            return phone_number

    # comment for commit (remove)


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
    subscription = db.relationship("Subscription", back_populates="orders")
    # Serializers
    serialize_rules = (
        "-user.orders",
        "-subscription.orders",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculate_total_monthly_price()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.calculate_total_monthly_price()

    def calculate_total_monthly_price(self):
        subscription = Subscription.query.get(self.subscription_id)
        if self.frequency == "Weekly":
            multiplier = 4
        elif self.frequency == "Bi-weekly":
            multiplier = 2
        else:  # Monthly
            multiplier = 1
        self.total_monthly_price = (
            subscription.price_per_box * self.quantity * multiplier
        )

    # Predefined values
    VALID_STATUSES = ["pending", "shipped", "delivered", "cancelled"]
    VALID_FREQUENCIES = ["Weekly", "Bi-weekly", "Monthly"]

    # Validation
    # @validates("status")
    # def validate_status(self, key, status):
    #     if not status:
    #         raise ValueError(f"{key} is required.")
    #     if status not in self.VALID_STATUSES:
    #         raise ValueError(f"Invalid {key}. Must be one of {self.VALID_STATUSES}.")
    #     return status

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
    name = db.Column(db.String)
    price_per_box = db.Column(db.Float)
    # Relationships
    orders = db.relationship(
        "Order", back_populates="subscription", cascade="all,delete"
    )
    box = db.relationship("Box", back_populates="subscription")
    # Serializers
    serialize_rules = ("-orders.subscription", "-box")

    # Validation
    @validates("name")
    def validate_description(self, key, value):
        if not value:
            raise ValueError(f"{key} is required.")
        else:
            return value

    @validates("price_per_box")  # new
    def validate_price_per_box(self, key, value):
        if value <= -0.01:
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
    image_url = db.Column(db.String)
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
