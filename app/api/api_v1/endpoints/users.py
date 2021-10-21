from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def get_users():
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Get Users!"})

@router.get("/{user_id}")
def read_item(user_id: int):
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": f"Get {user_id} User!"})