from litestar import Litestar, get, post


@get("/")
async def index() -> str:
    return "Hello, client!"


@post("/run")
async def post_run(command: str) -> dict[str, str]:

    return {
        "command": command,
        "result": "tbd",
    }


app = Litestar([index, post_run])
