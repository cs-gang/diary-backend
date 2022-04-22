from __future__ import annotations

from fastapi import FastAPI

from .__version__ import __version__ as version

app = FastAPI(title="Diary", version=version)


@app.route("/")
async def index() -> dict[str, str]:
    return {
        "message": f"Diary backend v{version}, by cs-gang. Source code at https://csgang.xyz/r/diary-backend"
    }
