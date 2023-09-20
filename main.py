import secrets

import flask
import requests


def generate_password(l):
    return secrets.token_hex(l)[:l - 1]


app = flask.Flask(__name__)


@app.route("/")
def index():
    return 'О ні, сторінка не знайдена!', 404


@app.route('/generate-password', methods=['POST'])
def generate_view():
    try:
        number = int(flask.request.form["numberPassword"])
    except (KeyError, ValueError):
        return flask.redirect('/')
    password = generate_password(number)
    return flask.render_template('generate.html', password=password)


@app.route("/api-show")
def api_view():
    r = requests.get("http://api.open-notify.org/astros.json")
    return


@app.errorhandler(404)
def page_not_found(error):
    return 'О ні, сторінка не знайдена!', 404


if __name__ == "__main__":
    app.run()

