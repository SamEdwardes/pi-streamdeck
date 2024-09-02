from pathlib import Path

from litestar import Litestar, get, post
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
from litestar.response import Template

@get("/")
async def index() -> Template:
    return Template(
        template_name="index.html", 
        context={
            "commands": [
                {
                    "name": "Hello world",
                    "command": "echo 'hello world'"
                },
                {
                    "name": "Hello world2",
                    "command": "echo 'hello world2'"
                },
            ]
        }
    )


@post("/run")
async def post_run(command: str) -> dict[str, str]:

    return {
        "command": command,
        "result": "tbd",
    }


app = Litestar(
    route_handlers=[index, post_run],
    template_config=TemplateConfig(
        directory=Path(__file__).parent / "templates",
        engine=JinjaTemplateEngine,
    ),
)
