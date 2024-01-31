from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    return '<p>Hello Flask!</p>'


if __name__ == '__main__':
    from waitress import serve

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # serve(app, host="0.0.0.0", port=80)
