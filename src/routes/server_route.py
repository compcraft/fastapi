from extensions import APIRouter
from controllers import server_controller

router = APIRouter(
    prefix="/server",
    tags=["server"],
    responses={404: {"description": "Not found"}},
)


@router.get('/')
def index():
    return server_controller.status()


@router.get('/status')
def status():
    return server_controller.status()


@router.get('/query')
def status():
    return server_controller.query()
