SCHEMA = [

# ==========================================================
# LENS
# ==========================================================

{
    "id": "lens",
    "label": "Lens",

    "fields": [

        {
            "id": "focal_length",
            "label": "Focal Length",
            "type": "combo",
            "values": [

                "24mm",
                "35mm",
                "50mm",
                "85mm",
                "105mm",
                "135mm"

            ]
        },

        {
            "id": "aperture",
            "label": "Aperture",
            "type": "combo",
            "values": [

                "f/1.2",
                "f/1.4",
                "f/1.8",
                "f/2",
                "f/2.8",
                "f/4"

            ]
        }

    ]
},

# ==========================================================
# SHOT
# ==========================================================

{
    "id": "shot",
    "label": "Shot",

    "fields": [

        {
            "id": "framing",
            "label": "Framing",
            "type": "combo",
            "values": [

                "extreme close-up",
                "close-up",
                "headshot",
                "portrait",
                "upper body",
                "half body",
                "three quarter body",
                "full body"

            ]
        }

    ]
},

# ==========================================================
# ANGLE
# ==========================================================

{
    "id": "angle",
    "label": "Angle",

    "fields": [

        {
            "id": "camera_angle",
            "label": "Camera Angle",
            "type": "combo",
            "values": [

                "eye level",
                "slightly above",
                "high angle",
                "low angle",
                "worm's eye view",
                "bird's eye view"

            ]
        }

    ]
},

# ==========================================================
# COMPOSITION
# ==========================================================

{
    "id": "composition",
    "label": "Composition",

    "fields": [

        {
            "id": "composition",
            "label": "Composition",
            "type": "combo",
            "values": [

                "centered composition",
                "rule of thirds",
                "symmetrical composition",
                "cinematic composition"

            ]
        }

    ]
},

# ==========================================================
# FOCUS
# ==========================================================

{
    "id": "focus",
    "label": "Focus",

    "fields": [

        {
            "id": "focus",
            "label": "Focus",
            "type": "combo",
            "values": [

                "sharp focus",
                "focus on eyes",
                "shallow depth of field",
                "deep depth of field"

            ]
        }

    ]
},

# ==========================================================
# STYLE
# ==========================================================

{
    "id": "style",
    "label": "Style",

    "fields": [

        {
            "id": "photo_style",
            "label": "Photo Style",
            "type": "combo",
            "values": [

                "photograph",
                "portrait photography",
                "fashion photography",
                "editorial photography",
                "studio photography",
                "cinematic still"

            ]
        }

    ]
}

]