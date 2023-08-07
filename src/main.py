from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    films = ["sa", "wdawd"]
    return render_template("main.html", films=films)


if __name__ == '__main__':
    app.run(debug=True)
