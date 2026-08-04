from .prompt_engine import PromptEngine


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
                "appearance": ("STRING",),
                "pose": ("STRING",),
                "scene": ("STRING",),
                "camera": ("STRING",),
                "quality": ("STRING",),
            }
        }

    def assemble(
        self,
        character,
        appearance=None,
        pose=None,
        scene=None,
        camera=None,
        quality=None,
    ):

        prompt = PromptEngine().assemble(
            character=character,
            appearance=appearance,
            pose=pose,
            scene=scene,
            camera=camera,
            quality=quality,
        )

        return (prompt,)