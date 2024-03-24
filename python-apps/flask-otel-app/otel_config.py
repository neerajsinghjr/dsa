# --- opentelemety traces library imports --- #
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.sampling import StaticSampler, Decision
from opentelemetry import trace
# --- coralogix sampler --- #
from coralogix_opentelemetry.trace.samplers import CoralogixTransactionSampler


# --- coralogix constants --- #
CX_ENDPOINT = 'ingress.coralogix.in:443'
CX_TOKEN = 'b995cb02-6fc5-a783-51c7-6abbedeee2ba'
CX_APPLICATION_NAME = '13karat'
CX_SUBSYSTEM_NAME = '13karat'


# --- coralogix headers --- #
headers = ', '.join([
    f'Authorization=Bearer%20{CX_TOKEN}',
    f'CX-Application-Name={CX_APPLICATION_NAME}',
    f'CX-Subsystem-Name={CX_SUBSYSTEM_NAME}'
])

# --- opentelemetry setup --- #
# resource creation;;
flask_resource = Resource.create({
    SERVICE_NAME: 'flask_test_resource'
})
# sampler to sample the incoming api data ;;
flask_sampler = CoralogixTransactionSampler(
    StaticSampler(Decision.RECORD_AND_SAMPLE)
)
# create tracer providers
tracer_provider = TracerProvider(
    resource=flask_resource,
    sampler=flask_sampler
)
# otlp exporter to transport spans to coralogix;;
exporter = OTLPSpanExporter(
    endpoint=CX_ENDPOINT,
    headers=headers
)
# set up a span processor to send spans to the exporter
span_processor = SimpleSpanProcessor(exporter)
# debugging the span
# span_processor = ConsoleSpanExporter(exporter)

# add the span processor to the tracer provider
tracer_provider.add_span_processor(span_processor)
trace.set_tracer_provider(tracer_provider)

tracer = trace.get_tracer_provider().get_tracer(__name__)