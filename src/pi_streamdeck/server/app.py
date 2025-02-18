from litestar import Litestar, get, post
import uvicorn


@get("/")
async def index() -> str:
    return "Hello, server!"


@post("/run")
async def post_run(command: str) -> dict[str, str]:

    return {
        "command": command,
        "result": "tbd",
    }


app = Litestar([index, post_run])

