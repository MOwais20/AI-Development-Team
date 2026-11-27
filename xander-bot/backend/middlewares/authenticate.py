from starlette.responses import JSONResponse
from fastapi import Request

import secrets
import os

ALLOWED_ROUTES = [
    "/",
    "/openapi.json",
    "/docs"
]

async def api_authenticate_key(request: Request, call_next):

    # Excluding Public Routes
    if request.url.path in ALLOWED_ROUTES:
        return await call_next(request)

    API_KEY = request.headers.get("X-API-KEY", "")
    OUR_API_KEY = os.getenv("AUTHENTICATED_KEY", "")

    # An unset AUTHENTICATED_KEY rejects everything instead of allowing everything
    if not OUR_API_KEY or not secrets.compare_digest(API_KEY.encode(), OUR_API_KEY.encode()):
        return JSONResponse(
            status_code=403, 
            content={
                "message": "Unauthorized Request"
            })

    return await call_next(request)