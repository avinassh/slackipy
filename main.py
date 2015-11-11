from flask import Flask
from flask_wtf.csrf import CsrfProtect

from views import IndexView


app = Flask(__name__)
CsrfProtect(app)
app.add_url_rule('/', view_func=IndexView.as_view('index'))


if __name__ == '__main__':
    app.run(debug=True)
