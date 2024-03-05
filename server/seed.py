#!/usr/bin/env python3

# Standard library imports
import random

# Local imports
from config import app, db
from models import User, Order, Subscription, Box

# Create Flask app context
app.app_context().push()


# Function to seed users
def seed_users():
    print("Seeding users...")
    for i in range(10):
        user = User(
            username=f"user_{i}",
            password="password123",  # may want to use a more secure method for generating passwords
            email=f"user_{i}@example.com",
            total_active_orders=random.randint(0, 5),
        )
        db.session.add(user)
    db.session.commit()
    print("Users seeded.")


# Function to seed subscriptions
def seed_subscriptions():
    print("Seeding subscriptions...")
    subscriptions = [
        {"description": "Basic Self-Care Package", "subtotal_price": 30.0},
        {"description": "Premium Beard Care Kit", "subtotal_price": 40.0},
        {"description": "Deluxe Hair Care Box", "subtotal_price": 35.0},
        {"description": "Ultimate Skincare Bundle", "subtotal_price": 50.0},
    ]
    for sub in subscriptions:
        subscription = Subscription(
            description=sub["description"], subtotal_price=sub["subtotal_price"]
        )
        db.session.add(subscription)
    db.session.commit()
    print("Subscriptions seeded.")


# Function to seed boxes
def seed_boxes():
    print("Seeding boxes...")
    boxes = [
        {
            "name": "Self-Care Essentials Box",
            "included_items": "This box contains a variety of self-care products, including face masks, bath salts, and scented candles.",
            "subscription_id": 1,
        },
        {
            "name": "Beard Grooming Kit",
            "included_items": "Inside this box, you'll find beard oil, beard balm, and a beard comb.",
            "subscription_id": 2,
        },
        {
            "name": "Hair Care Deluxe",
            "included_items": "This box is filled with premium hair care products, including shampoo, conditioner, and hair serum.",
            "subscription_id": 3,
        },
        {
            "name": "Skincare Essentials Box",
            "included_items": "In this box, you'll find a selection of skincare essentials, such as cleanser, moisturizer, and sunscreen.",
            "subscription_id": 4,
        },
        # Add more boxes here if needed
    ]
    for box in boxes:
        new_box = Box(
            name=box["name"],
            included_items=box["included_items"],
            subscription_id=box["subscription_id"],
        )
        db.session.add(new_box)
    db.session.commit()
    print("Boxes seeded.")


# Function to seed orders
# Function to seed orders
def seed_orders():
    print("Seeding orders...")
    users = User.query.all()
    subscriptions = Subscription.query.all()
    for _ in range(100):
        user = random.choice(users)
        subscription = random.choice(subscriptions)
        order = Order(
            user_id=user.id,
            subscription_id=subscription.id,
            status=random.choice(
                Order.VALID_STATUSES
            ),  # Use valid statuses from Order model
            frequency=random.choice(
                Order.VALID_FREQUENCIES
            ),  # Use valid frequencies from Order model
            quantity=random.randint(1, 10),
            total_monthly_price=random.uniform(10.0, 100.0),
        )
        db.session.add(order)
    db.session.commit()
    print("Orders seeded.")


if __name__ == "__main__":
    with app.app_context():
        print("Starting seed...")
        db.drop_all()  # Drop all tables
        db.create_all()  # Create all tables
        seed_users()
        seed_subscriptions()
        seed_boxes()
        seed_orders()
        print("Seed completed.")
