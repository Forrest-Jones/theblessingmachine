from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    donations = db.relationship('Donation', backref='user', lazy=True)
    organizations = db.relationship('Organization', secondary='user_org_association', backref='users', lazy=True)

user_org_association = db.Table('user_org_association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('org_id', db.Integer, db.ForeignKey('organization.id'), primary_key=True)
)

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    logo = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(80), nullable=False)
    goals = db.Column(db.String(255), nullable=False)
    achievements = db.Column(db.String(255), nullable=False)
    financial_needs = db.Column(db.String(255), nullable=False)
    success_stories = db.relationship('SuccessStory', backref='organization', lazy=True)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    frequency = db.Column(db.String(20), nullable=False)
    payment_info = db.Column(db.String(80), nullable=False)

class SuccessStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
