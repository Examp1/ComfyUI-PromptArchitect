class CameraPrompt:

    NAME = "camera"

    def build(self, data):

        result = []

        result += self.style(data)
        result += self.shot(data)
        result += self.angle(data)
        result += self.composition(data)
        result += self.lens(data)
        result += self.focus(data)

        return result

    # -------------------------------------------------
    # STYLE
    # -------------------------------------------------

    def style(self, data):

        result = []

        style = data.get("style", {})

        value = style.get("photo_style")

        mapping = {

            "photograph": "portrait photograph",

            "portrait photography": "portrait photography",

            "fashion photography": "fashion fashion editorial",

            "editorial photography": "editorial fashion photography",

            "studio photography": "professional studio photograph",

            "cinematic still": "cinematic still",

        }

        if value:

            result.append(mapping.get(value, value))

        return result

    # -------------------------------------------------
    # SHOT
    # -------------------------------------------------

    def shot(self, data):

        result = []

        shot = data.get("shot", {})

        framing = shot.get("framing")

        mapping = {

            "extreme close-up": "extreme close-up shot",

            "close-up": "close-up portrait",

            "headshot": "headshot portrait",

            "portrait": "portrait",

            "upper body": "upper body shot",

            "half body": "half body shot",

            "three quarter body": "three-quarter body shot",

            "full body": "full body shot",

        }

        if framing:

            result.append(mapping.get(framing, framing))

        return result

    # -------------------------------------------------
    # ANGLE
    # -------------------------------------------------

    def angle(self, data):

        result = []

        angle = data.get("angle", {})

        camera_angle = angle.get("camera_angle")

        mapping = {

            "eye level": "eye-level camera angle",

            "slightly above": "slightly elevated camera angle",

            "high angle": "high-angle shot",

            "low angle": "low-angle shot",

            "bird's eye view": "bird's-eye view",

            "worm's eye view": "worm's-eye view",

        }

        if camera_angle:

            result.append(mapping.get(camera_angle, camera_angle))

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
    # LENS
    # -------------------------------------------------

    def lens(self, data):

        result = []

        lens = data.get("lens", {})

        focal = lens.get("focal_length")

        aperture = lens.get("aperture")

        if focal:

            result.append(f"shot on a {focal} lens")

        if aperture:

            result.append(f"{aperture} aperture")

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