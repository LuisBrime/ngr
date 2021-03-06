import logging

from fastapi import FastAPI
from mangum import Mangum

from ngr.api.v1 import bodies

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI(title='NGR', openapi_prefix='/prod')


@app.get('/')
def health_check():
    return dict(message='Hello there!')


app.include_router(bodies.router)


def handler(event, context):
    logger.info('## EVENT')
    logger.info(event)

    asgi_handler = Mangum(app)
    response = asgi_handler(event, context)

    logger.info('## RESPONSE')
    logger.info(response)

    return response
