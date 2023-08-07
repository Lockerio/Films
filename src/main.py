from flask import Flask, render_template

from src.container import filmService
from src.utils.film_data_helper import FilmDataHelper

app = Flask(__name__)


@app.route("/")
def main():
    raw_films = filmService.get_all()
    films = FilmDataHelper.format_films(raw_films)

    return render_template("main.html", films=films)


if __name__ == '__main__':
    app.run(debug=True)
