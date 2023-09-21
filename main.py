import secrets
from flask import  Flask, request
from faker import Faker
import csv


def generate_password(l):
    return secrets.token_hex(l)[:l - 1]


app = Flask(__name__)
fake = Faker()

@app.route("/")
def index():
    return 'Головна сторінка'

@app.errorhandler(404)
def page_not_found(error):
    return 'О ні, сторінка не знайдена!', 404

@app.route("/requirements/", methods=['GET'])
def requirements():
    try:
        txt = ''
        with open("requrements.txt") as file:
            for line in file:
                txt += line + '<br>'
        return txt
    except:
        return ("File broken or not exists")


@app.route("/users/generate", methods=['GET'])
def generate_users():
    try:
        n = request.args.get("number")
        if n == None:
            n=""
        n = "100" if n == "" else n
        n = int(n)
        if n > 0 and n <= 1000:
            txt = ''
            for x in range(n):
                txt += fake.name() + " " + fake.email() + '<br>'
            return txt
        else:
            return ("Incorect query parameter")
    except:
        return ("Incorect query parameter")

@app.route("/mean/", methods=['GET'])
def mean():
    try:
        hight = 0
        weight = 0
        num = 0
        with open('hw.csv', 'r') as File:
            reader = csv.DictReader(File)
            for line in reader:
                num += 1
                hight += float(line[' "Height(Inches)"'])
                weight += float(line[' "Weight(Pounds)"'])
        hight = hight / num * 2.54
        weight = weight / num * 0.45359237
        hight_txt = "Average hight: " + str(hight) + " cm"
        weight_txt = "Average weight: " + str(weight) + " kg"
        return hight_txt + "<br>" + weight_txt
    except:
        return ("File broken or not exists")


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

