import sys
from os.path import dirname
import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.charts import Bar
from bokeh.charts.attributes import CatAttr
sys.path.append(dirname(__file__))
sys.path.append(dirname(dirname(__file__)))
from app.models import User, BudgetGroup, Expense

colors = ['firebrick', 'navy', 'forestgreen', 'goldenrod', 'chocolate1', 'purple']

PLOT_WIDTH = 420
PLOT_HEIGHT = 400


def group_query(group_name):
    users = User.query
    groups = BudgetGroup.query
    group = groups.filter_by(group_name=group_name).first()
    expenses = Expense.query.filter_by(group=group.id).all()

    expense_data = {'amount': [],
                    'user': [],
                    'domain': [],
                    'time': []}

    for exp in expenses:
        user = users.filter_by(id=exp.user).first()
        expense_data['amount'].append(getattr(exp, 'amount'))
        expense_data['user'].append(user.username)
        expense_data['time'].append(exp.timestamp)
        expense_data['domain'].append(exp.domain)

    expense_data = pd.DataFrame(expense_data)

    return expense_data


def common_expense_timeline(group_name):
    expense_data = group_query(group_name)

    source = {'amount': [],
              'color': [],
              'time': [],
              'user': []}

    for i, (user, df) in enumerate(expense_data.groupby('user')):
        source['amount'].append(list(df['amount'].values))
        source['time'].append(list(df['time'].values))
        source['color'].append(colors[i])
        source['user'].append(user)

    source = ColumnDataSource(data=source)

    fig = figure(x_axis_type='datetime', title='Expenses timeline', width=PLOT_WIDTH, height=PLOT_HEIGHT)

    fig.multi_line(xs='time', ys='amount', color='color', source=source, line_width=2)

    return fig


def common_expense_global_summary(group_name):
    expense_data = group_query(group_name)
    expense_data = expense_data[['amount', 'domain']].groupby('domain', as_index=False).sum()
    expense_data = expense_data.sort_values(by='amount', ascending=False).reset_index(drop=True)

    fig = Bar(expense_data,
              label=CatAttr(columns=['domain'], sort=False),
              values='amount',
              agg='sum',
              color='domain',
              title='Expenses summary (common)',
              width=PLOT_WIDTH,
              height=PLOT_HEIGHT)
    fig.legend.border_line_alpha = 0
    fig.legend.location = "bottom_left"
    fig.legend.background_fill_alpha = 0
    return fig


def common_expense_comparison(group_name):
    expense_data = group_query(group_name)

    fig = Bar(expense_data,
              label='user',
              stack='domain',
              values='amount',
              agg='sum',
              color='domain',
              bar_width=0.4,
              title='Expenses comparisons (common)',
              width=PLOT_WIDTH,
              height=PLOT_HEIGHT)

    fig.legend.border_line_alpha = 0
    fig.legend.location = "bottom_left"
    fig.legend.background_fill_alpha = 0
    return fig

