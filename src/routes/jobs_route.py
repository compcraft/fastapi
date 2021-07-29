from extensions import APIRouter
from controllers import jobs_controller
from libs.models import List, Job, User

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"],
    responses={404: {"description": "Not found"}},
)


# @router.get("/insert")
# def list_jobs():
#     return jobs_controller.insert_jobs()


@router.get("/", response_model=List[Job])
def list_jobs():
    return jobs_controller.list_all_jobs()


@router.get("/{job}", response_model=Job)
def get_job(job: str, limit: int = 10,  minimal: bool = False, toplist: bool = True):
    return jobs_controller.get_info_job(job, limit, minimal, toplist)


@router.get("/{job}/toplist", response_model=List[User])
def toplist_job(job: str, limit: int = 10):
    return jobs_controller.get_toplist_job(job, limit)
