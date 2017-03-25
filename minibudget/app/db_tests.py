import sys
from os.path import dirname
sys.path.append(dirname(__file__))
sys.path.append(dirname(dirname(__file__)))
from app import db
from app.models import User, BudgetGroup, Expense

brea = BudgetGroup('brea')
group2 = BudgetGroup('other')
db.session.add(brea)
db.session.add(group2)
db.session.commit()

groups = BudgetGroup.query
brea = groups.filter_by(group_name='brea').first()

gerome = User('gerome', brea)
siyu = User('siyu', brea)
db.session.add(gerome)
db.session.add(siyu)
db.session.commit()

# groups = BudgetGroup.query
# brea = groups.filter_by(group_name='brea').first()
# print(brea)
# #
# # users = User.query
# # gerome = users.filter_by(username='gerome').first()
# # # print(gerome)
# exp1 = Expense(24.32, gerome, brea, 'food')
# # db.session.add(exp1)
# # db.session.commit()
#
# exp = Expense.query.all()
# print(exp[3].amount)
