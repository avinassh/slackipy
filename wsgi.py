#!/usr/bin/python

import os


virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR', '.'), 'virtenv')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    exec_namespace = dict(__file__=virtualenv)
    with open(virtualenv, 'rb') as exec_file:
        file_contents = exec_file.read()
    compiled_code = compile(file_contents, virtualenv, 'exec')
    exec(compiled_code, exec_namespace)
except IOError:
    pass


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
