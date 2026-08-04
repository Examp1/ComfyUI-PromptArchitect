from aiohttp import web

from server import PromptServer

from ..schemas.character import SCHEMA as CHARACTER_SCHEMA
from ..schemas.appearance import SCHEMA as APPEARANCE_SCHEMA
from ..schemas.pose import SCHEMA as POSE_SCHEMA
from ..schemas.scene import SCHEMA as SCENE_SCHEMA
from ..schemas.camera import SCHEMA as CAMERA_SCHEMA


SCHEMAS = {

    "CharacterBuilder": CHARACTER_SCHEMA,

    "AppearanceBuilder": APPEARANCE_SCHEMA,

    "PoseBuilder": POSE_SCHEMA,

    "SceneBuilder": SCENE_SCHEMA,

    "CameraBuilder": CAMERA_SCHEMA,

}


@PromptServer.instance.routes.post("/promptarchitect/schema")
async def get_schema(request):

    body = await request.json()

    builder = body.get("builder")

    schema = SCHEMAS.get(builder)

    if schema is None:

        return web.json_response(
            {
                "success": False,
                "error": f"Unknown builder: {builder}"
            }
        )

    return web.json_response(
        {
            "success": True,
            "schema": schema,
        }
    )