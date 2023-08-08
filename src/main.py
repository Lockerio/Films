from flask import Flask, render_template, request, redirect, url_for

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


@app.route('/films_by_genre', methods=['POST'])
def films_by_genre():
    selected_genre = request.form.get('genre')
    films = filmService.get_all_by_genre(selected_genre)
    return render_template('films_by_genre.html', films=films, genre=selected_genre)


@app.route('/random_film', methods=['POST'])
def random_film():
    selected_genre = request.form.get('genre')
    film = filmService.get_random_one_by_genre(selected_genre)
    film_id = film.id
    return redirect(url_for("detail_film", film_id=film_id))


if __name__ == '__main__':
    app.run(debug=True)
