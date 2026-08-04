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
                "135mm",
                "200mm"

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
                "f/4",
                "f/5.6",
                "f/8"

            ]
        }

    ]
},

# ==========================================================
# CAMERA DISTANCE
# ==========================================================

{
    "id": "distance",
    "label": "Camera Distance",

    "fields": [

        {
            "id": "shot",
            "label": "Shot",
            "type": "combo",
            "values": [

                "extreme close-up",
                "close-up",
                "headshot",
                "portrait",
                "medium shot",
                "cowboy shot",
                "three-quarter shot",
                "full body shot",
                "long shot"

            ]
        }

    ]
},

# ==========================================================
# SUBJECT
# ==========================================================

{
    "id": "subject",
    "label": "Subject",

    "fields": [

        {
            "id": "position",
            "label": "Position",
            "type": "combo",
            "values": [

                "centered",
                "close to camera",
                "far from camera",
                "occupying most of the frame",
                "small subject"

            ]
        }

    ]
},

# ==========================================================
# CAMERA ANGLE
# ==========================================================

{
    "id": "angle",
    "label": "Camera Angle",

    "fields": [

        {
            "id": "camera_angle",
            "label": "Angle",
            "type": "combo",
            "values": [

                "eye level",
                "slightly above",
                "high angle",
                "low angle",
                "worm's eye view",
                "bird's eye view",
                "overhead",
                "dutch angle"

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
                "cinematic composition",
                "wide composition",
                "close composition",
                "negative space"

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
            "label": "Style",
            "type": "combo",
            "values": [

                "photograph",
                "portrait photography",
                "fashion photography",
                "beauty photography",
                "editorial photography",
                "studio photography",
                "commercial photography",
                "lifestyle photography",
                "cinematic still"

            ]
        }

    ]
}

]