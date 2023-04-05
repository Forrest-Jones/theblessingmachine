
from app import app, db
from models import User, Organization, Donation, SuccessStory

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    User.query.delete()
    Organization.query.delete()
    Donation.query.delete()
    SuccessStory.query.delete()

    print("Creating users...")
    user1 = User(name='John Doe', email='john.doe@example.com', password='password')
    user2 = User(name='Jane Smith', email='jane.smith@example.com', password='password')
    user3 = User(name='Bob Johnson', email='bob.johnson@example.com', password='password')
    users = [user1, user2, user3]

    print("Creating organizations...")
    org1 = Organization(name='Charity A', logo='logo.png', tagline='Helping those in need',
                        goals='Goal 1, Goal 2, Goal 3', achievements='Achievement 1, Achievement 2, Achievement 3',
                        financial_needs='Need 1, Need 2, Need 3')
    org2 = Organization(name='Charity B', logo='logo.png', tagline='Making a difference',
                        goals='Goal 1, Goal 2, Goal 3', achievements='Achievement 1, Achievement 2, Achievement 3',
                        financial_needs='Need 1, Need 2, Need 3')
    org3 = Organization(name='Charity C', logo='logo.png', tagline='Changing lives',
                        goals='Goal 1, Goal 2, Goal 3', achievements='Achievement 1, Achievement 2, Achievement 3',
                        financial_needs='Need 1, Need 2, Need 3')
    organizations = [org1, org2, org3]

    print("Creating donations...")
donation1 = Donation(user_id=user1.id, organization_id=org1.id, amount=50.00, frequency='monthly', payment_info='credit card')
donation2 = Donation(user_id=user2.id, organization_id=org2.id, amount=25.00, frequency='one-time', payment_info='paypal')
donation3 = Donation(user_id=user3.id, organization_id=org3.id, amount=100.00, frequency='monthly', payment_info='bank transfer')
donations = [donation1, donation2, donation3]

# set the user and organization IDs for the donations
donation1.user_id = user1.id
donation2.user_id = user2.id
donation3.user_id = user3.id
donation1.organization_id = org1.id
donation2.organization_id = org2.id
donation3.organization_id = org3.id

db.session.add_all(users)
db.session.add_all(organizations)
db.session.add_all(donations)
db.session.add_all(stories)
db.session.commit()

print("Seeding done!")

