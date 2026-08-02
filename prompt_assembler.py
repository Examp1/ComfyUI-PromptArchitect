from .assemblers.generic_prompt import GenericPrompt


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

        prompt = GenericPrompt().assemble(character)

        return (prompt,)