from flask import Flask
from flask_wtf.csrf import CSRFProtect

from .views import IndexView


app = Flask(__name__)
CSRFProtect(app)
app.add_url_rule('/', view_func=IndexView.as_view('index'))
app.config.from_envvar('SLACKIPY_CONFIG')


if __name__ == '__main__':
    app.run(debug=True)
