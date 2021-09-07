from flask.views import MethodView
from flask import request, render_template, current_app, jsonify

from .forms import InviteForm
from .slack import invite_user, get_team_name


class IndexView(MethodView):

    def get(self):
        team_id = current_app.config['SLACK_TEAM_ID']
        team_name = get_team_name()
        form = InviteForm(request.form)
        return render_template('index.html', form=form,
                               team_name=team_name, team_id=team_id)

    def post(self):
        form = InviteForm(request.form)
        email = form.email.data
        team_name = get_team_name()
        result = invite_user(email)
        return render_template('return.html',
                               team_name=team_name, result=result)
