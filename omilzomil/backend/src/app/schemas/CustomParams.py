from fastapi import Query
from fastapi_pagination import Params


class CustomParams(Params):
    page: int = Query(1, ge=1, description="Page number")
    size: int = Query(10, ge=1, le=100, description="Page size")
