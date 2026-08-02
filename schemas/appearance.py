SCHEMA = [

# ==========================================================
# HAIR
# ==========================================================

{
    "id": "hair",
    "label": "Hair",

    "fields": [

        {
            "id": "length",
            "label": "Length",
            "type": "combo",
            "values": [

                "short",
                "medium",
                "long",
                "very long"

            ]
        },

        {
            "id": "style",
            "label": "Style",
            "type": "combo",
            "values": [

                "loose hair",
                "messy bun",
                "bun",
                "ponytail",
                "high ponytail",
                "braid",
                "side braid",
                "twintails",
                "bob cut",
                "pixie cut",
                "wavy hair",
                "curly hair"

            ]
        }

    ]
},

# ==========================================================
# CLOTHING
# ==========================================================

{
    "id": "clothing",
    "label": "Clothing",

    "fields": [

        {
            "id": "outfit",
            "label": "Outfit",
            "type": "multiline"
        }

    ]
},

# ==========================================================
# ACCESSORIES
# ==========================================================

{
    "id": "accessories",
    "label": "Accessories",

    "fields": [

        {
            "id": "items",
            "label": "Items",
            "type": "multiline"
        }

    ]
},

# ==========================================================
# MAKEUP
# ==========================================================

{
    "id": "makeup",
    "label": "Makeup",

    "fields": [

        {
            "id": "style",
            "label": "Style",
            "type": "combo",
            "values": [

                "none",
                "light",
                "natural",
                "soft glam",
                "full glam"

            ]
        }

    ]
},

# ==========================================================
# NAILS
# ==========================================================

{
    "id": "nails",
    "label": "Nails",

    "fields": [

        {
            "id": "style",
            "label": "Style",
            "type": "multiline"
        }

    ]
},

# ==========================================================
# BODY DETAILS
# ==========================================================

{
    "id": "body_details",
    "label": "Body Details",

    "fields": [

        {
            "id": "details",
            "label": "Details",
            "type": "multiline"
        }

    ]
}

]