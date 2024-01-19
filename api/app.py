import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from .endpoints.healthz import router as healthz_router

app = FastAPI(title="db-x")


def create_app() -> FastAPI:
    logger = logging.getLogger(__name__)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logger.exception("API Exception", extra={"request": request})

        return JSONResponse(
            status_code=500,
            content={"message": "Oops! DB-X down!!"},
        )

    logger.info("Creating DB-X app")

    return app


app.include_router(healthz_router)

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=6400)
