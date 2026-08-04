from ..core.prompt_data import PromptData


class DatasetGenerator:

    CATEGORY = "Prompt Architect"

    RETURN_TYPES = (
        "STRING",  # character
        "STRING",  # appearance
        "STRING",  # pose
        "STRING",  # scene
        "STRING",  # camera
        "STRING",  # variation
    )

    RETURN_NAMES = (
        "character",
        "appearance",
        "pose",
        "scene",
        "camera",
        "variation",
    )

    FUNCTION = "generate"

    @classmethod
    def INPUT_TYPES(cls):

        return {
            "required": {

                "character": ("STRING",),

                "appearance": ("STRING",),

                "pose": ("STRING",),

                "scene": ("STRING",),

                "camera": ("STRING",),

                "variation_fields": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": (
                            "pose.body.position\n"
                            "appearance.hair.style\n"
                            "scene.location"
                        ),
                    },
                ),

            }
        }

    # -------------------------------------------------

    def generate(

        self,

        character,
        appearance,
        pose,
        scene,
        camera,
        variation_fields,

    ):

        character = PromptData(character)
        appearance = PromptData(appearance)
        pose = PromptData(pose)
        scene = PromptData(scene)
        camera = PromptData(camera)

        print("\n========== BEFORE ==========\n")
        print(pose)

        pose.set(
            "body.position",
            "kneeling",
        )

        print("\n========== AFTER ==========\n")
        print(pose)

        return (
            character.serialize(),
            appearance.serialize(),
            pose.serialize(),
            scene.serialize(),
            camera.serialize(),
            variation_fields,
        )