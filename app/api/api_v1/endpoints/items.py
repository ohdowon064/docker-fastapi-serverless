from typing import Optional

from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/")
def read_item():
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Get Items!"})


@router.get("/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": f"Get {item_id} Item! And Query String is '{q}'"})
