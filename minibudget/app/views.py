from flask import Blueprint, render_template
from flask_restful import Api, Resource, reqparse
from app import db, models
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


@api_bp.route('/')
@api_bp.route('/index')
def index():
    return "Hello, World!"


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
                                 personal=args['common'])

        db.session.add(expense)
        db.session.commit()

        expenses = models.Expense.query.all()

        for exp in expenses:
            print(exp.group, exp.domain, exp.amount)

        return args


api.add_resource(ExpenseManager, '/add_expense', methods=['POST'])
