import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

from .views import IndexView

app = Flask(__name__, template_folder=os.path.join(__path__[0], 'templates'))
CSRFProtect(app)
app.add_url_rule('/', view_func=IndexView.as_view('index'))

if os.environ.get('SLACKIPY_CONFIG', None) is not None:
    app.config.from_envvar('SLACKIPY_CONFIG')


if __name__ == '__main__':
    app.run(debug=True)
