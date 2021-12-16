from flask import Flask, render_template
from flask.templating import render_template_string
from webapp.weather import weather_by_city
from webapp.python_news_org import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    @app.route('/')
    def index():
        title = "HOBOSTI"
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        news_list = get_python_news()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

    return app
 