SCHEMA = [
    # ==========================================================
    # BASIC
    # ==========================================================
    {
        "id": "basic",
        "label": "Basic",
        "fields": [
            {
                "id": "gender",
                "label": "Gender",
                "type": "combo",
                "values": ["woman", "man"],
            },
            {
                "id": "age",
                "label": "Age",
                "type": "combo",
                "values": ["18-20", "20-22", "22-25", "25-30", "30-35"],
            },
        ],
    },
    # ==========================================================
    # SKIN
    # ==========================================================
    {
        "id": "skin",
        "label": "Skin",
        "fields": [
            {
                "id": "tone",
                "label": "Tone",
                "type": "combo",
                "values": ["fair", "light", "tan", "dark"],
            },
            {
                "id": "texture",
                "label": "Texture",
                "type": "combo",
                "values": ["clear", "smooth", "freckled", "slightly tanned"],
            },
        ],
    },
    # ==========================================================
    # EYES
    # ==========================================================
    {
        "id": "eyes",
        "label": "Eyes",
        "fields": [
            {
                "id": "color",
                "label": "Color",
                "type": "combo",
                "values": ["emerald green", "green", "blue", "brown", "hazel", "gray"],
            },
            {
                "id": "shape",
                "label": "Shape",
                "type": "combo",
                "values": ["round", "almond", "cat"],
            },
            {
                "id": "lashes",
                "label": "Lashes",
                "type": "combo",
                "values": ["short", "natural", "long natural", "long", "thick"],
            },
        ],
    },
    # ==========================================================
    # FACE
    # ==========================================================
    {
        "id": "face",
        "label": "Face",
        "fields": [
            {
                "id": "shape",
                "label": "Shape",
                "type": "combo",
                "values": ["oval", "round", "heart"],
            },
            {
                "id": "jaw",
                "label": "Jawline",
                "type": "combo",
                "values": ["soft", "defined", "sharp"],
            },
            {
                "id": "nose",
                "label": "Nose",
                "type": "combo",
                "values": ["small straight", "button", "slim"],
            },
            {
                "id": "lips",
                "label": "Lips",
                "type": "combo",
                "values": ["thin", "natural", "full natural", "plump"],
            },
        ],
    },
    # ==========================================================
    # HAIR
    # ==========================================================
    {
        "id": "hair",
        "label": "Hair",
        "fields": [
            {
                "id": "color",
                "label": "Color",
                "type": "combo",
                "values": [
                    "black",
                    "brown",
                    "blonde",
                    "copper red",
                    "auburn",
                    "white",
                    "pink",
                ],
            }
        ],
    },
    # ==========================================================
    # BODY
    # ==========================================================
    {
        "id": "body",
        "label": "Body",
        "fields": [
            {
                "id": "physique",
                "label": "Physique",
                "type": "combo",
                "values": ["petite", "slim feminine", "athletic", "curvy"],
            },
            {
                "id": "figure",
                "label": "Figure",
                "type": "combo",
                "values": ["hourglass", "pear", "rectangle"],
            },
            {
                "id": "breasts",
                "label": "Breasts",
                "type": "combo",
                "values": [
                    "AA cup",
                    "A cup",
                    "B cup",
                    "C cup",
                    "D cup",
                    "E cup",
                    "F cup",
                ],
            },
        ],
    },
]
