from pathlib import Path
from typing import Annotated, Any

import httpx
from litestar import Litestar, get, post
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.enums import RequestEncodingType
from litestar.params import Body
from litestar.response import Template
from litestar.template.config import TemplateConfig
from loguru import logger


@get("/")
async def index() -> Template:
    logger.info("Loading index...")
    return Template(
        template_name="index.html",
        context={
            "commands": [
                {"name": "Hello world", "command": "echo hello world"},
                {"name": "Crazy command!!!", "command": "echo crazy command!!"},
                {"name": "Whats up doc?", "command": "echo whats up doc?"},
            ]
        },
    )


@post("/run")
async def post_run(
    data: Annotated[dict[str, str], Body(media_type=RequestEncodingType.URL_ENCODED)],
) -> dict[str, str]:
    logger.info(f"Running command: {data['command']=}")
    command = data["command"]
    with httpx.Client(base_url="http://samedwardes-64g2:8000") as client:
        r = client.post("/run", json={"command": command})
        logger.info(r.status_code)
        logger.info(r.text)

    return {
        "command": command,
        "result": r.text,
    }


app = Litestar(
    route_handlers=[index, post_run],
    template_config=TemplateConfig(
        directory=Path(__file__).parent / "templates",
        engine=JinjaTemplateEngine,
    ),
)
