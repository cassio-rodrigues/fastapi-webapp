import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.home.indexviewmodel import IndexViewModel

router = fastapi.APIRouter()


@router.get("/")
@template(template_file="home/index.html")
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/about")
@template(template_file="home/about.html")
def about():
    return {
        # "package_count": 240789,
        # "release_count": 170667,
        # "user_count": 4,
        # "packages": [
        #     {"id": "fastAPI", "summary": "A great web framework"},
        #     {"id": "uvicorn", "summary": "A great ASGI server"},
        #     {"id": "httpx", "summary": "Requests used in a async way"},
        # ]
    }
