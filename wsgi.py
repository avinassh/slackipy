#!/usr/bin/python

import os

from main import app as application

application.config['slack_team_name'] = os.environ['slack_team_name']
application.config['slack_api_token'] = os.environ['slack_api_token']
application.config['SECRET_KEY'] = os.environ['flask_app_secret']

# Below for testing locally only
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
