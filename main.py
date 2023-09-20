import secrets
import flask
import requests
import faker


def generate_password(l):
    return secrets.token_hex(l)[:l - 1]


app = flask.Flask(__name__)


@app.route("/")
def index():
    return 'Головна сторінка'

@app.errorhandler(404)
def page_not_found(error):
    return 'О ні, сторінка не знайдена!', 404

@app.route("/requirements/", methods=['GET'])
def requirements():
    txt = ''
    with open("requrements.txt") as file:
        for line in file:
            txt += line + '<br>'
    return txt



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





if __name__ == "__main__":
    app.run()

