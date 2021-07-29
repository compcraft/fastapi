from extensions import APIRouter
from controllers import mcmmo_controller

router = APIRouter(
    prefix="/mcmmo",
    tags=["mcmmo"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def list_skills():
    return mcmmo_controller.list_skills()


@router.get("/{skill}")
def toplist_skill(skill: str, limit: int = 10):
    return mcmmo_controller.toplist_skill(skill, limit)
