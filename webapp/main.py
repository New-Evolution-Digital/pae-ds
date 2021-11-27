from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, JSONResponse
from fastapi.requests import Request
import uvicorn

from webapp.api import routing
from webapp.utilities.security.header_checking import get_api_key

app = FastAPI(
    title="New Evolution Auto",
    description="REST api for New Evolution",
    version="0.1",
    docs_url="/"
)

app.include_router(routing.router, tags=['Submission'], dependencies=[Security(get_api_key)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app)