from .prompt_module import PromptModule


class PosePrompt(PromptModule):

    NAME = "character"

    RULES = {

        "body.position":
            "{value}",

        "head.position":
            "{value}",

        "eyes.direction":
            "{value}",

        "expression.type":
            "{value}",

        "arms.position":
            "{value}",

        "legs.position":
            "{value}",

        "interaction.action":
            "{value}",

        "extra.details":
            "{value}",

        "custom.prompt":
            "{value}",

    }
