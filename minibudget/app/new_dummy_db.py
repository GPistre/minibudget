import os
import sys
from os.path import dirname
sys.path.append(dirname(__file__))
sys.path.append(dirname(dirname(__file__)))
from app import db
from app.models import User, BudgetGroup, Expense
import random

try:
    os.remove('../app.db')
except FileNotFoundError:
    pass

import db_create
import db_tests

brea = BudgetGroup('brea')
group2 = BudgetGroup('other')
db.session.add(brea)
db.session.add(group2)
db.session.commit()

groups = BudgetGroup.query
brea = groups.filter_by(group_name='bread').first()

gerome = User('gerome', brea)
siyu = User('siyu', brea)
db.session.add(gerome)
db.session.add(siyu)
db.session.commit()

groups = BudgetGroup.query
brea = groups.filter_by(group_name='brea').first()

users = User.query
gerome = users.filter_by(username='gerome').first()

for i in range(30):
    exp1 = Expense(random.random() * 20,
                   random.choice([gerome, siyu]),
                   brea,
                   random.choice(['food', 'voyages', 'restaurant', 'commande', 'autres']),
                   True)
    db.session.add(exp1)
    db.session.commit()
