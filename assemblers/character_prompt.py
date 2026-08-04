from .prompt_module import PromptModule


class CharacterPrompt(PromptModule):

    NAME = "character"

    RULES = {
        "basic.gender": "young {value}",
        "basic.age": "{value} years old",
        "skin": lambda x: f"{x['tone']} {x['texture']} skin",
        "eyes.color": "{value} eyes",
        "eyes.shape": "{value} eyes",
        "eyes.lashes": "{value} eyelashes",
        "face.shape": "soft {value} face",
        "face.jaw": "{value} jawline",
        "face.nose": "{value} nose",
        "face.lips": "{value} lips",
        "hair.color": "{value} hair",
        "body.physique": "{value} physique",
        "body.figure": "{value} figure",
        "body.breasts": "{value} sized breasts",
    }
