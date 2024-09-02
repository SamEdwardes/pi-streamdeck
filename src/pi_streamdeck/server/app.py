from typing import Annotated, Any

from litestar import Litestar, get, post
from litestar.enums import RequestEncodingType
from litestar.params import Body
from loguru import logger


@get("/")
async def index() -> str:
    return "Hello, server!"


@post("/run")
async def post_run(
    data: Annotated[dict[str, str], Body()],
) -> dict[str, str]:
    logger.info(data)
    command = data["command"]
    logger.info(f"Received command {command}")
    return {
        "command": command,
        "result": command,
    }


app = Litestar([index, post_run])
