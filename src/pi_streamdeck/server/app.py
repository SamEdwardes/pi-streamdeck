from typing import Annotated

from litestar import Litestar, get, post
from litestar.params import Body
from loguru import logger
import sh

from rich import inspect


@get("/")
async def index() -> str:
    return "Hello, server!"


def command_is_safe(command: str) -> bool:
    if "sudo" in command.lower():
        logger.warning("Command contains sudo, not running.")
        return False
    else:
        logger.info("Command deemed safe, going to run it.")
        return True


@post("/run")
async def post_run(
    data: Annotated[dict[str, str], Body()],
) -> dict[str, str]: 
    logger.info(data)
    command_str = data["command"]
    logger.info(f"Received command: `{command_str}`")

    if not command_is_safe(command_str):
        raise ValueError("Command deemed not safe!")

    try:
        command = sh.Command('/bin/bash')
        logger.info(f"{command=}")
        output = command('-c', command_str)
        logger.info(f"{output=}")
        if not isinstance(output, str):
            raise ValueError("Command did not run")

    except Exception as e:
        inspect(e)
        raise ValueError("Failed...")

    
    return {
        "command": command_str,
        "output": output,
    }

app = Litestar([index, post_run])
