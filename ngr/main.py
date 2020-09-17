from fastapi import FastAPI

from ngr.api.v1 import bodies

app = FastAPI()

app.include_router(bodies.router)
