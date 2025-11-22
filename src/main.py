from fastapi import FastAPI

from src.routes import auth_routes, event_routes, me_routes

app = FastAPI(title="Event Booking API")


app.include_router(auth_routes.router)
app.include_router(event_routes.router)
app.include_router(me_routes.router)
