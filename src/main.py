from flask import Flask, render_template

from src.container import filmService

app = Flask(__name__)


@app.route("/")
def main():
    films = filmService.get_all()
    return render_template("main.html", films=films)


if __name__ == '__main__':
    app.run(debug=True)
