SCHEMA = [


{
    "id": "body",
    "label": "Body",

    "fields": [

        {
            "id": "position",
            "label": "Body Position",
            "type": "combo",
            "values": [
                "none",
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


{
    "id": "head",
    "label": "Head",

    "fields": [

        {
            "id": "position",
            "label": "Head Position",
            "type": "combo",
            "values": [
                "none",
                "looking straight",
                "looking down",
                "looking up",
                "head tilted left",
                "head tilted right"

            ]
        }

    ]
},



{
    "id": "eyes",
    "label": "Eyes",

    "fields": [

        {
            "id": "direction",
            "label": "Eye Direction",
            "type": "combo",
            "values": [
                "none",
                "looking at camera",
                "looking at viewer",
                "looking away",
                "eyes closed"

            ]
        }

    ]
},



{
    "id": "expression",
    "label": "Expression",

    "fields": [

        {
            "id": "type",
            "label": "Expression",
            "type": "combo",
            "values": [
                "none",
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



{
    "id": "arms",
    "label": "Arms",

    "fields": [

        {
            "id": "position",
            "label": "Arm Position",
            "type": "combo",
            "values": [
                "none",
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


{
    "id": "legs",
    "label": "Legs",

    "fields": [

        {
            "id": "position",
            "label": "Leg Position",
            "type": "combo",
            "values": [
                "none",
                "legs together",
                "crossed legs",
                "one leg forward",
                "wide stance"

            ]
        }

    ]
},


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