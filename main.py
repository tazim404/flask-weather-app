from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/search')
def search():
    mode = 'json'
    name_of_city = request.args.get('city')
    resposne = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={name_of_city}&appid=c475420553c0af07f96f399b6becdc1c&mode={mode}')
    data = resposne.json()
    try:
        icon_data = data['weather'][0]['icon']
    except Exception:
        return "Invalid City Name"
    return render_template('result.html', data=data, icon_data=icon_data)


@app.errorhandler(404)
def error(e):
    return render_template('error.html')


app.run(debug=True)
