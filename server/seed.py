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
    names = [
        "John Doe",
        "Jane Smith",
        "Alice Johnson",
        "Bob Brown",
        "Charlie Davis",
        "Diana Evans",
        "Ethan Foster",
        "Grace Harris",
        "Ivan Garcia",
        "Julia Hernandez",
    ]
    for i in range(10):
        user = User(
            username=f"user_{i}",
            password="password123",  # may want to use a more secure method for generating passwords
            email=f"user_{i}@example.com",
            address=f"1234 Example St, Apt {i}",
            full_name=names[i],  # Use actual names
            phone_number=f"555-555-{i}{i}{i}{i}",
            total_active_orders=random.randint(0, 5),
            admin=False if i != 0 else True,  # first user is admin
        )
        db.session.add(user)
    db.session.commit()
    print("Users seeded.")


# Function to seed subscriptions
def seed_subscriptions():
    print("Seeding subscriptions...")
    subscriptions = [
        {
            "name": "Basic Self-Care Package",
            "price_per_box": 30.0,
        },
        {
            "name": "Premium Beard Care Kit",
            "price_per_box": 40.0,
        },
        {
            "name": "Deluxe Hair Care Box",
            "price_per_box": 35.0,
        },
        {
            "name": "Ultimate Skincare Bundle",
            "price_per_box": 50.0,
        },
    ]
    for sub in subscriptions:
        subscription = Subscription(
            name=sub["name"], price_per_box=sub["price_per_box"]
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
            "image_url": "https://i.etsystatic.com/29479462/r/il/75915f/3191580298/il_794xN.3191580298_23yl.jpg",
        },
        {
            "name": "Beard Grooming Kit",
            "included_items": "Inside this box, you'll find beard oil, beard balm, and a beard comb.",
            "subscription_id": 2,
            "image_url": "https://i.etsystatic.com/19259100/r/il/e41d62/2162011475/il_794xN.2162011475_3hbb.jpg",
        },
        {
            "name": "Hair Care Deluxe",
            "included_items": "This box is filled with premium hair care products, including shampoo, conditioner, and hair serum.",
            "subscription_id": 3,
            "image_url": "https://i.etsystatic.com/36842034/r/il/0b9248/5673959767/il_794xN.5673959767_ju1z.jpg",
        },
        {
            "name": "Skincare Essentials Box",
            "included_items": "In this box, you'll find a selection of skincare essentials, such as cleanser, everyday skin care, and anti-aging products.",
            "subscription_id": 4,
            "image_url": "https://i.etsystatic.com/13826775/r/il/504425/5380229319/il_794xN.5380229319_co44.jpg",
        },
        # Add more boxes here if needed
    ]
    for box in boxes:
        new_box = Box(
            name=box["name"],
            included_items=box["included_items"],
            subscription_id=box["subscription_id"],
            image_url=box["image_url"],
        )
        db.session.add(new_box)
    db.session.commit()
    print("Boxes seeded.")


# Function to seed orders
def seed_orders():
    print("Seeding orders...")
    users = User.query.all()
    subscriptions = Subscription.query.all()
    frequency_mapping = {
        "Monthly": 1,
        "Bi-weekly": 2,
        "Weekly": 4,
    }  # add more if needed
    for _ in range(3):
        user = random.choice(users)
        subscription = random.choice(subscriptions)
        quantity = random.randint(1, 10)
        frequency_str = random.choice(Order.VALID_FREQUENCIES)
        frequency_num = frequency_mapping[frequency_str]
        total_monthly_price = subscription.price_per_box * quantity * frequency_num
        order = Order(
            user_id=user.id,
            subscription_id=subscription.id,
            status=random.choice(Order.VALID_STATUSES),
            frequency=frequency_str,
            quantity=quantity,
            total_monthly_price=total_monthly_price,
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
