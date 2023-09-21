from flask import  Flask, request, render_template
from faker import Faker
import csv
import requests

app = Flask(__name__)
fake = Faker()

@app.route("/", methods=['GET'])
def index():
    return 'Main'

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
        return ("File is broken or does not exist")


@app.route("/users/generate/", methods=['GET'])
def generate_users():
    try:
        arr = []
        n = request.args.get("number")
        n = "100" if n == None or n == "" else n
        try:
            n = int(n)
        except:
            return ("Incorect query parameter")

        if n > 0 and n <= 10000:
            for x in range(n):
                arr.append(fake.name() + " " + fake.email())
            return render_template('generateUsers.html', comments=arr)
        else:
            return ("Incorect query parameter")
    except:
        return ("Something went wrong")

@app.route("/mean/", methods=['GET'])
def mean():
    try:
        height = 0
        weight = 0
        num = 0
        with open('hw.csv', 'r') as File:
            reader = csv.DictReader(File)
            for line in reader:
                num += 1
                height += float(line[' "Height(Inches)"'])
                weight += float(line[' "Weight(Pounds)"'])
        height = height / num * 2.54
        weight = weight / num * 0.45359237
        height_txt = "Average height: " + str(height) + " cm"
        weight_txt = "Average weight: " + str(weight) + " kg"
        return height_txt + "<br>" + weight_txt
    except:
        return ("Something went wrong")

@app.route("/space/", methods=['GET'])
def space():
    try:
        number_of_cosmonauts = requests.get('http://api.open-notify.org/astros.json').json()['number']
        return "Number of cosmonauts in space: " + str(number_of_cosmonauts)
    except:
        return ("Something went wrong")


if __name__ == "__main__":
    app.run()
