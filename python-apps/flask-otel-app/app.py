# --- flask instrumentor --- #
from opentelemetry.instrumentation.flask import FlaskInstrumentor
# --- flask otel configuration imports --- #
import otel_config as otel
# --- flask app runtime imports --- #
from random import randint
from flask import Flask


# --- intialize the flask app --- #
app = Flask(__name__)

# --- initializing the flask instrumenter --- #
FlaskInstrumentor().instrument_app(app)


# --- basic application layer logic only --- #
@app.route("/roll")
def roll():
    res = dice()
    # span = trace.get_current_span()
    # span.set_attribute("roll.value", res) # Set custom tags
    return {
        'message': f"you rolled {res}"
    }


@otel.tracer.start_as_current_span("diceFunc")
def dice():
    return randint(1, 6)


if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 5050
    debug = True
    app.run(
        host=ip,
        port=port,
        debug=True
    )
