SCHEMA = [

# ==========================================================
# LOCATION
# ==========================================================

{
    "id": "scene",
    "label": "Scene",

    "fields": [

        {
            "id": "location",
            "label": "Location",
            "type": "combo",
            "values": [
                
                "studio",
                "bedroom",
                "living room",
                "bathroom",
                "kitchen",
                "office",
                "cafe",
                "restaurant",
                "street",
                "park",
                "forest",
                "beach",
                "mountains",
                "balcony",
                "hotel room"

            ]
        },

# ==========================================================
# LIGHTING
# ==========================================================

        {
            "id": "lighting",
            "label": "Lighting",
            "type": "combo",
            "values": [

                "soft studio lighting",
                "hard studio lighting",

                "window light",
                "soft window light",

                "natural daylight",

                "morning sunlight",
                "afternoon sunlight",

                "golden hour lighting",
                "sunset lighting",
                "blue hour lighting",

                "overcast daylight",

                "cinematic lighting",
                "dramatic lighting",

                "rim lighting",
                "backlighting",

                "warm ambient light",
                "cold ambient light",

                "neon lighting",

                "candle light",
                "fire light",

                "moonlight"

            ]
        },

# ==========================================================
# SCENE DETAILS
# ==========================================================

        {
            "id": "details",
            "label": "Scene Details",
            "type": "multiline"
        }

    ]
}

]