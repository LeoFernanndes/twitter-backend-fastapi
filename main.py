# from fastapi import FastAPI
# from starlette.requests import Request
# from starlette.responses import Response, JSONResponse
# from profiles import routes as profile_routes
# from tweets import routes as tweet_routes
# from services import database_connection
# from decouple import config

# database_connection.Base.metadata.create_all(bind=database_connection.engine)

# api = FastAPI()


# @api.get('/')
# async def healthcheck(request: Request):
#     return JSONResponse({"msg": "Ok."}, status_code=200)


# @api.get('/api-config')
# async def api_config(request: Request):
#     database_config = {
#         'DB_USER': config('DB_USER'),
#         'DB_PASSWORD': config('DB_PASSWORD'),
#         'DB_HOST': config('DB_HOST'),
#         'DB_PORT': config('DB_PORT'),
#         'DB_DATABASE': config('DB_DATABASE'),
#     }

#     config_dict = {
#         'database': database_config
#     }
#     return JSONResponse(config_dict, status_code=200)


# @api.get('/healthcheck')
# async def healthcheck(request: Request):
#     return JSONResponse({"response": "Api ok."}, status_code=200)


# api.include_router(profile_routes.router)
# api.include_router(tweet_routes.router)



"""FastAPI Application factory with OpenTelemetry instrumentation
sent to Jaeger in dev and to DataDog in staging and production."""

import uvicorn
# from opentelemetry import trace
# from opentelemetry.exporter.zipkin.json import ZipkinExporter
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.resources import Resource
# from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from fastapi import FastAPI
# from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
# from opentelemetry.sdk.trace.export import BatchSpanProcessor
from profiles import routes as profile_routes
from tweets import routes as tweet_routes
from profiles import models as profile_models
from tweets import models as tweet_models
from services.database_connection import SessionLocal
from services.database_connection import engine


app = FastAPI(root_path='/api')

# tracer = trace.get_tracer(__name__)

# zipkin_exporter = ZipkinExporter(
#     endpoint="http://localhost:9411/api/v2/spans"
# )

# zipkin_exporter = ZipkinExporter(
#     # version=Protocol.V2
#     # optional:
#     endpoint="http://localhost:9411/api/v2/spans",
#     # local_node_ipv4="192.168.0.1",
#     # local_node_ipv6="2001:db8::c001",
#     # local_node_port=31313,
#     # max_tag_value_length=256
#     # timeout=5 (in seconds)
# )

# span_processor = SimpleSpanProcessor(zipkin_exporter)
# trace_provider = TracerProvider(resource=Resource.create({"service.name": "open-telemetry-test"}))
# trace_provider.add_span_processor(span_processor)

@app.get('/opentelemetry-fastapi')
def about():
    # span = trace.get_current_span()
    # span.add_event("event message", {"event_attributes": 1})
    return "hello"

app.include_router(profile_routes.router)
app.include_router(tweet_routes.router)

# FastAPIInstrumentor.instrument_app(app,
#                                    tracer_provider=trace_provider)

if __name__ == "__main__":
    profile_models.Base.metadata.create_all(bind=engine)
    tweet_models.Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=8000)