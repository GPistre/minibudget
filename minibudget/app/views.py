from flask import Blueprint, render_template
from flask_restful import Api, Resource, reqparse
from app import db, models
from bokeh.layouts import row
from bokeh.embed import components
from plots import *
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


@api_bp.route('/')
@api_bp.route('/index')
def index():
    return "Usage : http://site_address/group/<group_name>"


@api_bp.route('/group/<group_name>')
def group_view(group_name):
    groups = models.BudgetGroup.query.filter_by(group_name=group_name).first()

    if groups:
        try:
            summary = common_expense_global_summary(group_name)
            timeline = common_expense_timeline(group_name)
            comparison = common_expense_comparison(group_name)

            script, div = components(row(summary, timeline, comparison))

            return render_template('index.html', group_name=group_name.capitalize(), script=script, plots_div=div)
        except:
            return 'no expenses yet'
    else:
        return 'No such group'


class GroupManager(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument('expense',
                                   type=float,
                                   required=True)

        super(GroupManager, self).__init__()

    def post(self):
        pass


class ExpenseManager(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('expense',
                                   type=float,
                                   required=True)

        self.reqparse.add_argument('budgetGroup',
                                   type=str,
                                   required=True)

        self.reqparse.add_argument('user',
                                   type=str,
                                   required=True)

        self.reqparse.add_argument('domain',
                                   type=str,
                                   required=True)

        self.reqparse.add_argument('common',
                                   type=int,
                                   required=True)

        super(ExpenseManager, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()

        groups = models.BudgetGroup.query
        user_group = groups.filter_by(group_name=args['budgetGroup']).first()

        users = models.User.query
        user = users.filter_by(username=args['user']).first()

        # check if user pwd is correct

        # check if user belongs to group

        expense = models.Expense(amount=args['expense'],
                                 user=user,
                                 group=user_group,
                                 domain=args['domain'],
                                 common=args['common'])

        db.session.add(expense)
        db.session.commit()

        expenses = models.Expense.query.all()

        for exp in expenses:
            print(exp.group, exp.domain, exp.amount)

        return args


api.add_resource(ExpenseManager, '/add_expense', methods=['POST'])
