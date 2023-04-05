from app import app, db
from app import User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

fake = Faker()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///theblessingmachine.db'
db = SQLAlchemy(app)


def seed_database():
    # Clear the existing data
    User.query.delete()
    Organization.query.delete()
    Donation.query.delete()
    SuccessStory.query.delete()

    # Generate fake Users
    for _ in range(20):
        user = User(
            name=fake.name(),
            email=fake.email(),
            password=fake.password(),
            address=fake.address()
        )
        db.session.add(user)

    # Generate fake Organizations
    for _ in range(10):
        organization = Organization(
            name=fake.company(),
            logo=fake.image_url(),
            tagline=fake.catch_phrase(),
            goals=fake.text(),
            achievements=fake.text(),
            financial_needs=fake.text()
        )
        db.session.add(organization)

    db.session.commit()

    # Generate fake Donations
    users = User.query.all()
    organizations = Organization.query.all()

    for _ in range(50):
        donation = Donation(
            user_id=random.choice(users).id,
            organization_id=random.choice(organizations).id,
            amount=random.uniform(10, 500),
            frequency=random.choice(['one-time', 'monthly', 'yearly']),
            payment_info=fake.credit_card_number()
        )
        db.session.add(donation)

    # Generate fake Success Stories
    for organization in organizations:
        for _ in range(3):
            success_story = SuccessStory(
                organization_id=organization.id,
                title=fake.sentence(),
                description=fake.paragraph()
            )
            db.session.add(success_story)

    db.session.commit()

if __name__ == '__main__':
    seed_database()