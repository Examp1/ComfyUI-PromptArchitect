from .schema_index import SchemaIndex

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

    def generate(
        self,
        character,
        appearance,
        pose,
        scene,
        camera,
        variation_fields,
    ):
        index = SchemaIndex()

        print("\n========== INDEX ==========\n")

        for key, value in index.items():

            print(key)
            print(value)
            print()

        print("\n===========================\n")

        return (
            character,
            appearance,
            pose,
            scene,
            camera,
            variation_fields,
        )
