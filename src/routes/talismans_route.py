from extensions import APIRouter
from controllers import talismans_controller

router = APIRouter(
    prefix="/talismans",
    tags=["talismans"],
    responses={404: {"description": "Not found"}},
)


# @router.get("/insert")
# async def insert_all():
#     return talismans_controller.insert_talismans()


@router.get("/")
def read_root(categories: bool = False):
    return talismans_controller.list_talismans(categories)


@router.get("/{category}")
def read_root(category: str):
    return talismans_controller.list_category_talismans(category)
