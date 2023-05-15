from fastapi import APIRouter
from app.routes.apis import *

api_router = APIRouter()

api_router.include_router(route_api.router)