from flask.views import MethodView
from flask import request, render_template, current_app, jsonify

from forms import InviteForm
from slack import invite_user


class Index(MethodView):

    def get(self):
        team_name = current_app.config['slack_team_name']
        form = InviteForm(request.form)
        return render_template('index.html', form=form, team_name=team_name)

    def post(self):
        form = InviteForm(request.form)
        email = form.email.data
        return jsonify(invite_user(email))
