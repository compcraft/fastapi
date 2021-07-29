from routes import (
    shop_route,
    server_route,
    enchantments_route,
    players_route,
    jobs_route,
    mcmmo_route,
    talismans_route
)
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(shop_route.router)
app.include_router(server_route.router)
app.include_router(enchantments_route.router)
app.include_router(players_route.router)
app.include_router(jobs_route.router)
app.include_router(talismans_route.router)
app.include_router(mcmmo_route.router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def docs():
    response = RedirectResponse(url="https://compcraft.baraus.dev/")
    return response
