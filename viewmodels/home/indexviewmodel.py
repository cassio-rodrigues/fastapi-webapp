from typing import List

from starlette.requests import Request

from services import package_service, user_service
from viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__int__(request)

        self.package_count: int = package_service.package_count()
        self.release_count: int = package_service.release_count()
        self.user_count: int = user_service.user_count()
        self.packages: List = package_service.latest_packages(limit=5)

    #     "package_count": 240789,
    #     "release_count": 170667,
    #     "user_count": 4,
    #     "packages": [
    #         {"id": "fastAPI", "summary": "A great web framework"},
    #         {"id": "uvicorn", "summary": "A great ASGI server"},
    #         {"id": "httpx", "summary": "Requests used in a async way"},
    #     ]
    #
    # }
