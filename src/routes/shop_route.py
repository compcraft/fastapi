from extensions import APIRouter
from controllers import shop_controller

router = APIRouter(
    prefix="/shops",
    tags=["shops"],
    responses={404: {"description": "Not found"}},
)


# @router.get("/insert")
# async def insert_all():
#     return shop_controller.insert_all()


@router.get("/{section}")
def read_root(section: str):
    return shop_controller.list_items_section(section=section)


@router.get("/")
def read_root():
    return shop_controller.list_items()
