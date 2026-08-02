class CameraPrompt:

    NAME = "camera"

    def build(self, data):

        result = []

        result += self.lens(data)
        result += self.shot(data)
        result += self.angle(data)
        result += self.composition(data)
        result += self.focus(data)
        result += self.style(data)

        return result

    # -------------------------------------------------
    # LENS
    # -------------------------------------------------

    def lens(self, data):

        result = []

        lens = data.get("lens", {})

        focal = lens.get("focal_length")
        aperture = lens.get("aperture")

        if focal:
            result.append(f"{focal} lens")

        if aperture:
            result.append(aperture)

        return result

    # -------------------------------------------------
    # SHOT
    # -------------------------------------------------

    def shot(self, data):

        result = []

        shot = data.get("shot", {})

        framing = shot.get("framing")

        if framing:
            result.append(framing)

        return result

    # -------------------------------------------------
    # ANGLE
    # -------------------------------------------------

    def angle(self, data):

        result = []

        angle = data.get("angle", {})

        camera_angle = angle.get("camera_angle")

        if camera_angle:
            result.append(camera_angle)

        return result

    # -------------------------------------------------
    # COMPOSITION
    # -------------------------------------------------

    def composition(self, data):

        result = []

        composition = data.get("composition", {})

        value = composition.get("composition")

        if value:
            result.append(value)

        return result

    # -------------------------------------------------
    # FOCUS
    # -------------------------------------------------

    def focus(self, data):

        result = []

        focus = data.get("focus", {})

        value = focus.get("focus")

        if value:
            result.append(value)

        return result

    # -------------------------------------------------
    # STYLE
    # -------------------------------------------------

    def style(self, data):

        result = []

        style = data.get("style", {})

        value = style.get("photo_style")

        if value:
            result.append(value)

        return result