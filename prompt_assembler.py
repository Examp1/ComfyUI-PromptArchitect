from .assemblers.generic_prompt import GenericPrompt
from .schemas.character import SCHEMA


class PromptAssembler:

    CATEGORY = "Prompt Architect"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)

    FUNCTION = "assemble"

    @classmethod
    def INPUT_TYPES(cls):

        return {

            "required": {

                "character": ("STRING",)

            }

        }

    def assemble(self, character):

        assembler = GenericPrompt(SCHEMA)

        return (
            assembler.assemble(character),
        )