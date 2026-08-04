from .data_manipulator import DataManipulator
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
        m = DataManipulator()

        print("\n====== BEFORE ======")
        print(pose)

        m.set(
            pose,
            "body.position",
            "kneeling"
        )

        print("\n====== AFTER ======")
        print(pose)
        
        return (
            character,
            appearance,
            pose,
            scene,
            camera,
            variation_fields,
        )
