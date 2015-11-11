import json
from slackipycore import invite, get_team_info
from slackipycore import (AlreadyInTeam, InvalidInviteeEmail,
                          InvalidAuthToken, AlreadyInvited, APIRequestError)
from flask import current_app


def invite_user(email):
    api_token = current_app.config['SLACK_API_TOKEN']
    team_id = current_app.config['SLACK_TEAM_ID']
    try:
        if invite(team_id=team_id, api_token=api_token,
                  invitee_email=email):
            return {'status': 'success'}
    except (AlreadyInTeam, InvalidInviteeEmail, InvalidAuthToken,
            AlreadyInvited, APIRequestError) as e:
        return _response_message(message=str(e))


def get_team_name():
    api_token = current_app.config['SLACK_API_TOKEN']
    team_id = current_app.config['SLACK_TEAM_ID']
    team_info = get_team_info(team_id=team_id, api_token=api_token)
    return team_info['name']


def _response_message(message):
    return {'status': 'fail', 'error': message}
