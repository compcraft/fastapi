from extensions import APIRouter
from controllers import enchantments_controller
from libs.models import Enchantment, List

router = APIRouter(
    prefix="/enchantments",
    tags=["enchantments"],
    responses={404: {"description": "Not found"}}
)


# @router.get('/verify', response_model=List[Enchantment], status_code=200)
# def verify():
#     return enchantments_controller.verify_enchantments()


@router.get('/custom', response_model=List[Enchantment], status_code=200)
def custom():
    return enchantments_controller.list_custom_enchantments()


@router.get('/default', response_model=List[Enchantment], status_code=200)
def custom():
    return enchantments_controller.list_default_enchantments()
