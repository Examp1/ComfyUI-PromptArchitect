from .prompt_module import PromptModule


class ScenePrompt(PromptModule):

    NAME = "scene"

    RULES = {

        "scene.location":
            "{value}",

        "scene.lighting":
            "{value}",

        "scene.details":
            "{value}",

    }