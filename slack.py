import json
from slackipycore import invite
from slackipycore import (AlreadyInTeam, InvalidInviteeEmail,
                          InvalidAuthToken, AlreadyInvited, APIRequestError)
from flask import current_app


def invite_user(email):
    api_token = current_app.config['slack_api_token']
    team_name = current_app.config['slack_team_name']
    try:
        if invite(team_name=team_name, api_token=api_token,
                  invitee_email=email):
            return json.dumps({'status': 'success'})
    except (AlreadyInTeam, InvalidInviteeEmail, InvalidAuthToken,
            AlreadyInvited, APIRequestError) as e:
        return _response_message(message=str(e))


def _response_message(message):
    return {'status': 'fail', 'error': message}
