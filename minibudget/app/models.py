from app import db
from datetime import datetime
# from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    budget_group = db.Column(db.Integer, db.ForeignKey('budget_group.id'))

    def __init__(self, username, group):
        self.username = username
        self.budget_group = group.id

    def __repr__(self):
        return '<User {0}>'.format(self.username)

    def add_budget_group(self, group):
        self.budget_group = group.id


class BudgetGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(64), index=True)
    users = db.relationship('User', lazy='dynamic')

    def __init__(self, name):
        self.group_name = name

    def __repr__(self):
        return '<BudgetGroup {0} id: {1}>'.format(self.group_name, self.id)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    group = db.Column(db.Integer, db.ForeignKey('budget_group.id'))
    timestamp = db.Column(db.DateTime)
    common = db.Column(db.Integer)
    domain = db.Column(db.String(64))

    def __init__(self, amount, user, group, domain, common):
        self.amount = amount
        self.user = user.id
        self.group = group.id
        self.domain = domain
        self.common = common
        self.timestamp = datetime.now()

