from flask import Flask, render_template

from src.container import filmService
from src.utils.film_data_helper import FilmDataHelper

app = Flask(__name__)
filmDataHelper = FilmDataHelper()

@app.route("/")
def main():
    raw_films = filmService.get_all()
    films = filmDataHelper.format_films(raw_films)
    return render_template("main.html", films=films)


@app.route("/film/<int:film_id>")
def detail_film(film_id):
    raw_film = filmService.get_one(film_id)
    film = filmDataHelper.format_film(raw_film)
    return render_template("detail_film.html", film=film)


if __name__ == '__main__':
    app.run(debug=True)
