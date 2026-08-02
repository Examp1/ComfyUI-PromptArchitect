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
                "character": ("STRING",),
            },

            "optional": {
                "pose": ("STRING",),
                "clothing": ("STRING",),
                "scene": ("STRING",),
                "camera": ("STRING",),
                "quality": ("STRING",),
            }
        }

    def assemble(
        self,
        character,
        pose=None,
        clothing=None,
        scene=None,
        camera=None,
        quality=None,
    ):

        prompt = GenericPrompt().assemble(
            character=character,
            pose=pose,
            clothing=clothing,
            scene=scene,
            camera=camera,
            quality=quality,
        )

        return (prompt,)