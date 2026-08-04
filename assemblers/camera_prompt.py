from .prompt_module import PromptModule


class CameraPrompt(PromptModule):

    NAME = "camera"

    RULES = {

        "style.photo_style": {

            "photograph": "professional photograph",

            "portrait photography": "professional portrait photograph",

            "fashion photography": "fashion editorial photograph",

            "beauty photography": "professional beauty photograph",

            "editorial photography": "editorial fashion photograph",

            "studio photography": "professional studio photograph",

            "commercial photography": "commercial photograph",

            "lifestyle photography": "lifestyle photograph",

            "cinematic still": "cinematic still",

        },


        "distance.shot": {

            "extreme close-up": "extreme close-up shot",

            "close-up": "close-up shot",

            "headshot": "headshot",

            "portrait": "portrait shot",

            "medium shot": "medium shot",

            "cowboy shot": "cowboy shot",

            "three-quarter shot": "three-quarter shot",

            "full body shot": "full body shot",

            "long shot": "long shot",

        },


        "subject.position": {

            "centered": "subject centered",

            "close to camera": "subject close to camera",

            "far from camera": "subject far from camera",

            "occupying most of the frame": "subject occupying most of the frame",

            "small subject": "small subject in frame",

        },


        "angle.camera_angle": {

            "eye level": "eye-level camera angle",

            "slightly above": "slightly elevated camera angle",

            "high angle": "high-angle shot",

            "low angle": "low-angle shot",

            "bird's eye view": "bird's-eye view",

            "worm's eye view": "worm's-eye view",

            "overhead": "overhead shot",

            "dutch angle": "dutch angle",

        },

        "composition.composition":
            "{value}",

        "lens.focal_length":
            "shot on a {value} lens",

        "lens.aperture":
            "{value} aperture",
            
        "focus.focus":
            "{value}",

    }