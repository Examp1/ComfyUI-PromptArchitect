from .prompt_module import PromptModule


class PosePrompt(PromptModule):

    NAME = "pose"

    RULES = {

        "body.position":
            "{value}",

        "legs.position":
            "{value}",

        "head.position":
            "{value}",

        "eyes.direction":
            "{value}",

        "arms.position":
            "{value}",

        "expression.type":
            "{value}",

        "interaction.action":
            "{value}",

        "extra.details":
            "{value}",

        "custom.prompt":
            "{value}",

    }