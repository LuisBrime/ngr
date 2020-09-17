from fastapi import APIRouter

from ngr.db import db

router = APIRouter()


@router.get('/bodies/', tags=['bodies'])
def get_bodies():
    return dict(data=db.read_data())


@router.get('/bodies/planets', tags=['bodies'])
def get_planets():
    data = db.read_data()
    planets = [planet for planet in data if planet['isPlanet']]
    return dict(data=planets)


@router.get('/bodies/{name}', tags=['bodies'])
def get_body(name: str):
    data = db.read_data()
    body = [
        body
        for body in data
        if body['name'] == name or body['name'].startswith(name.upper())
    ]
    print(body)
    return dict(data=body)
