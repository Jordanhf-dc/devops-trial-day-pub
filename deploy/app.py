import math
import os
import socket
import time
import flask
from datetime import datetime
from random import random

app = flask.Flask(__name__)


def estimate_pi(throws):
    """
    Calculate Pi to simulate some load

    throws: total number of darts to throw
    """

    # Number of darts that land inside.
    inside = 0

    # Iterate for the number of darts.
    for i in range(0, throws):
        # Generate random x, y in [0, 1].
        x2 = random() ** 2
        y2 = random() ** 2
        # Increment if inside unit circle.
        if math.sqrt(x2 + y2) < 1:
            inside += 1

    # inside / throws = pi / 4
    pi = (float(inside) / throws) * 4
    return pi


@app.route("/")
def pi():
    start = time.time()

    throws = int(os.environ.get("PI_THROWS", 100000))
    pi = estimate_pi(throws)

    duration = time.time() - start

    response = flask.Response(
        "<h1>Pi Simulation</h1>"
        f"<p>Calculating Pi using a Monte Carlo simulation</p>"
        f"<p>Running on {socket.gethostname()} at {datetime.now()}</p>"
        f"<p><strong>Estimated Pi ~= {pi:0.5f} in {duration:0.3f}s after {throws} throws</strong></p>"
    )

    response.headers["Cache-Control"] = "max-age=60"
    return response


@app.route("/error")
def error():
    """This view solely exists to purposely trigger an error"""
    raise NotImplementedError("You've triggered the error!")


if __name__ == "__main__":
    app.run()
