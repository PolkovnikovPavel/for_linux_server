from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/likly_plases')
def likly_plases():
    return render_template("likly_plases.html")


@app.route('/first_cliker')
def first_cliker():
    return render_template("first_cliker.html")


@app.route('/first_canvas')
def first_canvas():
    return render_template("first_canvas.html")


@app.route('/fibanachi')
def fibanachi():
    return render_template("fibanachi.html")


@app.route('/car_game')
def car_game():
    return render_template("car_game.html")


if __name__ == '__main__':
    from waitress import serve

    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)
    # serve(app, host="0.0.0.0", port=80)
