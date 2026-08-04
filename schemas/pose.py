SCHEMA = [

{
    "id": "settings",
    "label": "Settings",

    "fields": [

        {
            "id": "mode",
            "label": "Mode",
            "type": "combo",
            "values": [

                "preset",
                "custom"

            ]
        }

    ]
},

# ==========================================
# BODY
# ==========================================

{
    "id": "body",
    "label": "Body",

    "fields": [

        {
            "id": "position",
            "label": "Body Position",
            "type": "combo",
            "values": [

                "standing",
                "walking",
                "running",
                "sitting",
                "kneeling",
                "lying",
                "leaning",
                "squatting"

            ]
        }

    ]
},

# ==========================================
# HEAD
# ==========================================

{
    "id": "head",
    "label": "Head",

    "fields": [

        {
            "id": "position",
            "label": "Head Position",
            "type": "combo",
            "values": [

                "looking straight",
                "looking down",
                "looking up",
                "head tilted left",
                "head tilted right"

            ]
        }

    ]
},

# ==========================================
# EYES
# ==========================================

{
    "id": "eyes",
    "label": "Eyes",

    "fields": [

        {
            "id": "direction",
            "label": "Eye Direction",
            "type": "combo",
            "values": [

                "looking at camera",
                "looking at viewer",
                "looking away",
                "eyes closed"

            ]
        }

    ]
},

# ==========================================
# EXPRESSION
# ==========================================

{
    "id": "expression",
    "label": "Expression",

    "fields": [

        {
            "id": "type",
            "label": "Expression",
            "type": "combo",
            "values": [

                "neutral expression",
                "soft smile",
                "big smile",
                "serious expression",
                "confident expression",
                "seductive expression",
                "shy expression"

            ]
        }

    ]
},

# ==========================================
# ARMS
# ==========================================

{
    "id": "arms",
    "label": "Arms",

    "fields": [

        {
            "id": "position",
            "label": "Arm Position",
            "type": "combo",
            "values": [

                "arms at sides",
                "hands behind back",
                "arms crossed",
                "hands on hips",
                "one hand on hip",
                "one hand touching hair",
                "one hand touching face"

            ]
        }

    ]
},

# ==========================================
# LEGS
# ==========================================

{
    "id": "legs",
    "label": "Legs",

    "fields": [

        {
            "id": "position",
            "label": "Leg Position",
            "type": "combo",
            "values": [

                "legs together",
                "crossed legs",
                "one leg forward",
                "wide stance"

            ]
        }

    ]
},

# ==========================================
# INTERACTION
# ==========================================

{
    "id": "interaction",
    "label": "Interaction",

    "fields": [

        {
            "id": "action",
            "label": "Action",
            "type": "multiline"
        }

    ]
},

# ==========================================
# EXTRA
# ==========================================

{
    "id": "extra",
    "label": "Extra",

    "fields": [

        {
            "id": "details",
            "label": "Extra Details",
            "type": "multiline"
        }

    ]
},

# ==========================================
# CUSTOM
# ==========================================

{
    "id": "custom",
    "label": "Custom Prompt",

    "fields": [

        {
            "id": "prompt",
            "label": "Pose Prompt",
            "type": "multiline"
        }

    ]
}

]