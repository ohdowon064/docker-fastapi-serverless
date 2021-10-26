from os import getenv

import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from starlette import status
from starlette.responses import JSONResponse
from app.api.api_v1.api import router as v1_router


def create_app():
    # root_path = f"/{getenv('stage', '')}"
    app = FastAPI(
        # root_path=root_path,
        title="FastAPI + Docker + AWS Lambda",
        description="This is super fancy, with auto docs and everything!",
        version="0.1.0"
    )

    @app.get("/")
    def read_root():
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=dict(Hello="World"))

    app.include_router(v1_router, prefix="/api/v1")

    return app


app = create_app()
handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
