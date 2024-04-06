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


@otel.tracer.start_as_current_span("diceRoll")
def dice():
    return randint(1, 6)

# --- basic application layer logic only --- #
@app.route("/roll")
def roll():
    res = dice()
    span = otel.trace.get_current_span()
    span.set_attribute("roll.value", res) # Set custom tags
    return {
        'message': f"you rolled {res}"
    }

# --- Manual Instrumentation of coralogix span --- #
tracer = otel.trace.get_tracer_provider().get_tracer(__name__)
@app.route("/profile")
def profile():
    with tracer.start_as_current_span("appProfile") as span:
        def _profile(): return 'Neeraj Singh'
        def _logger(): return 'Coralogix'
        def _product(): return '13Karat'

        a = _profile()
        b = _logger()
        c = _product()

        span.set_attribute("appProfile.a", a)
        span.set_attribute("appProfile.b", b)
        span.set_attribute("appProfile.c", c)

        return {
            'status': 'ok',
            'data': {
                'a': a, 'b': b, 'c': c
            }
        }


if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 5050
    debug = True
    app.run(
        host=ip,
        port=port,
        debug=True
    )
