SCHEMA = [

{
    "id": "scene",

    "fields": [

        {
            "id": "location",
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

        {
            "id": "lighting",
            "type": "combo",
            "values": [
                "soft studio lighting",
                "natural lighting",
                "window lighting",
                "golden hour lighting",
                "sunset lighting",
                "blue hour lighting",
                "overcast lighting",
                "cinematic lighting",
                "dramatic lighting",
                "neon lighting"
            ]
        },

        {
            "id": "time",
            "type": "combo",
            "values": [
                "morning",
                "afternoon",
                "golden hour",
                "sunset",
                "blue hour",
                "night"
            ]
        },

        {
            "id": "weather",
            "type": "combo",
            "values": [
                "clear sky",
                "cloudy",
                "rainy",
                "snowing",
                "foggy",
                "stormy"
            ]
        },

        {
            "id": "atmosphere",
            "type": "combo",
            "values": [
                "cozy",
                "romantic",
                "luxury",
                "minimalistic",
                "casual",
                "warm",
                "cold",
                "summer vibes",
                "winter vibes"
            ]
        },

        {
            "id": "props",
            "type": "multiline"
        },

        {
            "id": "extra",
            "type": "multiline"
        }

    ]
}

]