SCHEMA = [

{
    "id": "scene",
    "label": "Scene",

    "fields": [

        # ==========================================
        # LOCATION
        # ==========================================

        {
            "id": "location",
            "label": "Location",
            "type": "combo",
            "values": [

                "Studio",
                "Bedroom",
                "Living Room",
                "Bathroom",
                "Kitchen",
                "Office",
                "Cafe",
                "Restaurant",
                "Street",
                "Park",
                "Forest",
                "Beach",
                "Mountains",
                "Balcony",
                "Hotel Room"

            ]
        },

        # ==========================================
        # LIGHTING
        # ==========================================

        {
            "id": "lighting",
            "label": "Lighting",
            "type": "combo",
            "values": [

                "Soft Studio Lighting",
                "Natural Lighting",
                "Window Lighting",
                "Golden Hour Lighting",
                "Sunset Lighting",
                "Blue Hour Lighting",
                "Overcast Lighting",
                "Cinematic Lighting",
                "Dramatic Lighting",
                "Neon Lighting"

            ]
        },

        # ==========================================
        # TIME OF DAY
        # ==========================================

        {
            "id": "time",
            "label": "Time Of Day",
            "type": "combo",
            "values": [

                "Morning",
                "Afternoon",
                "Golden Hour",
                "Sunset",
                "Blue Hour",
                "Night"

            ]
        },

        # ==========================================
        # WEATHER
        # ==========================================

        {
            "id": "weather",
            "label": "Weather",
            "type": "combo",
            "values": [

                "Clear Sky",
                "Cloudy",
                "Rainy",
                "Snowing",
                "Foggy",
                "Stormy"

            ]
        },

        # ==========================================
        # ATMOSPHERE
        # ==========================================

        {
            "id": "atmosphere",
            "label": "Atmosphere",
            "type": "combo",
            "values": [

                "Cozy",
                "Romantic",
                "Luxury",
                "Minimalistic",
                "Casual",
                "Warm",
                "Cold",
                "Summer Vibes",
                "Winter Vibes"

            ]
        },

        # ==========================================
        # PROPS
        # ==========================================

        {
            "id": "props",
            "label": "Props",
            "type": "multiline"
        },

        # ==========================================
        # EXTRA DETAILS
        # ==========================================

        {
            "id": "extra",
            "label": "Extra Details",
            "type": "multiline"
        }

    ]
}

]