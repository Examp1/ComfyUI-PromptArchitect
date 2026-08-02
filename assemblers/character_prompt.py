
class CharacterPrompt:

    NAME = "character"

    def build(self, data):

        result = []

        result += self.basic(data)
        result += self.skin(data)
        result += self.eyes(data)
        result += self.face(data)
        result += self.hair(data)
        result += self.body(data)

        return result

    # -------------------------------------------------
    # BASIC
    # -------------------------------------------------

    def basic(self, data):

        result = []

        basic = data.get("basic", {})

        gender = basic.get("gender")
        age = basic.get("age")

        if gender:
            result.append(f"young {gender}")

        if age:
            result.append(f"{age} years old")

        return result

    # -------------------------------------------------
    # SKIN
    # -------------------------------------------------

    def skin(self, data):

        result = []

        skin = data.get("skin", {})

        tone = skin.get("tone")
        texture = skin.get("texture")

        parts = []

        if tone:
            parts.append(tone)

        if texture:
            parts.append(texture)

        if parts:
            result.append(" ".join(parts) + " skin")

        return result

    # -------------------------------------------------
    # EYES
    # -------------------------------------------------

    def eyes(self, data):

        result = []

        eyes = data.get("eyes", {})

        color = eyes.get("color")
        shape = eyes.get("shape")
        lashes = eyes.get("lashes")

        if color:
            result.append(f"{color} eyes")

        if shape:
            result.append(f"{shape} eyes")

        if lashes:
            result.append(f"{lashes} eyelashes")

        return result

    # -------------------------------------------------
    # FACE
    # -------------------------------------------------

    def face(self, data):

        result = []

        face = data.get("face", {})

        shape = face.get("shape")
        jaw = face.get("jaw")
        nose = face.get("nose")
        lips = face.get("lips")

        if shape:
            result.append(f"soft {shape} face")

        if jaw:
            result.append(f"{jaw} jawline")

        if nose:
            result.append(f"{nose} nose")

        if lips:
            result.append(f"{lips} lips")

        return result

    # -------------------------------------------------
    # HAIR
    # -------------------------------------------------

    def hair(self, data):

        result = []

        hair = data.get("hair", {})

        color = hair.get("color")

        if color:
            result.append(f"{color} hair")

        return result

    # -------------------------------------------------
    # BODY
    # -------------------------------------------------

    def body(self, data):

        result = []

        body = data.get("body", {})

        physique = body.get("physique")
        figure = body.get("figure")
        breasts = body.get("breasts")

        if physique:
            result.append(f"{physique} physique")

        if figure:
            result.append(f"{figure} figure")

        if breasts:
            result.append(breasts)

        return result