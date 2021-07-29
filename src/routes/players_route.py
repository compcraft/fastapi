from extensions import APIRouter
from controllers import players_controller

router = APIRouter(
    prefix="/players",
    tags=["players"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def list_players():
    return players_controller.list_all_players()


@router.get("/playedtime")
def list_players(limit: int = 10):
    return players_controller.toplist_playedtime(limit)


@router.get("/balance")
def list_players(limit: int = 10):
    return players_controller.toplist_balance(limit)


@router.get("/{player_username}/mcmmo")
def player_stats_mcmmo(player_username: str):
    return players_controller.player_mcmmo(username=player_username)


@router.get("/{player_username}/jobs")
def player_stats_jobs(player_username: str):
    return players_controller.player_jobs(username=player_username)
