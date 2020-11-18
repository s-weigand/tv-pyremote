"""Server implementation."""
from flask import Flask, render_template

from tv_pyremote.api.v1 import init_api

app = Flask(__name__)


@app.route("/")
def home():
    """Render server root."""
    return render_template("index.html")


init_api(app)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
