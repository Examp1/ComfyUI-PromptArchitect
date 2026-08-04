from .prompt_module import PromptModule


class AppearancePrompt(PromptModule):

    NAME = "appearance"

    RULES = {

        # -------------------------------------------------
        # HAIR
        # -------------------------------------------------

        "hair.style":
            "{value} hairstyle",

        # -------------------------------------------------
        # CLOTHING
        # -------------------------------------------------

        "clothing.outfit":
            "wearing {value}",

        # -------------------------------------------------
        # ACCESSORIES
        # -------------------------------------------------

        "accessories.items":
            "wearing {value}",

        # -------------------------------------------------
        # MAKEUP
        # -------------------------------------------------

        "makeup.style": {

            "none": None,

            "light": "light makeup",

            "natural": "natural makeup",

            "soft glam": "soft glam makeup",

            "full glam": "full glam makeup",

        },

        # -------------------------------------------------
        # NAILS
        # -------------------------------------------------

        "nails.style":
            lambda value: f"{value.strip()} nail polish",

        # -------------------------------------------------
        # BODY DETAILS
        # -------------------------------------------------

        "body_details.details":
            "{value}",

    }