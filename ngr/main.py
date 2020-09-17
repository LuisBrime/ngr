from fastapi import FastAPI
from mangum import Mangum

from ngr.api.v1 import bodies

app = FastAPI()

app.include_router(bodies.router)

handler = Mangum(app)
