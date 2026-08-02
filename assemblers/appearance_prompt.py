class AppearancePrompt:

    NAME = "appearance"

    def build(self, data):

        result = []

        result += self.hair(data)
        result += self.clothing(data)
        result += self.accessories(data)
        result += self.makeup(data)
        result += self.nails(data)
        result += self.body_details(data)

        return result

    # -------------------------------------------------
    # HAIR
    # -------------------------------------------------

    def hair(self, data):

        result = []

        hair = data.get("hair", {})

        style = hair.get("style")

        if style:

            result.append(f"{style} hairstyle")

        return result

    # -------------------------------------------------
    # CLOTHING
    # -------------------------------------------------

    def clothing(self, data):

        result = []

        clothing = data.get("clothing", {})

        outfit = clothing.get("outfit")

        if outfit:

            result.append(f"wearing {outfit}")

        return result

    # -------------------------------------------------
    # ACCESSORIES
    # -------------------------------------------------

    def accessories(self, data):

        result = []

        accessories = data.get("accessories", {})

        items = accessories.get("items")

        if items:

            result.append(f"wearing {items}")

        return result

    # -------------------------------------------------
    # MAKEUP
    # -------------------------------------------------

    def makeup(self, data):

        result = []

        makeup = data.get("makeup", {})

        style = makeup.get("style")

        if style and style != "none":

            result.append(f"{style} makeup")

        return result

    # -------------------------------------------------
    # NAILS
    # -------------------------------------------------

    def nails(self, data):

        result = []

        nails = data.get("nails", {})

        style = nails.get("style")

        if style:

            style = style.strip()

            result.append(f"{style} nail polish")

        return result

    # -------------------------------------------------
    # BODY DETAILS
    # -------------------------------------------------

    def body_details(self, data):

        result = []

        body = data.get("body_details", {})

        details = body.get("details")

        if details:

            result.append(details)

        return result