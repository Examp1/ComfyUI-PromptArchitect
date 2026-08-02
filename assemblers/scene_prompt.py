class ScenePrompt:

    NAME = "scene"

    def build(self, data):

        result = []

        result += self.location(data)
        result += self.lighting(data)
        result += self.time(data)
        result += self.weather(data)
        result += self.atmosphere(data)
        result += self.props(data)
        result += self.extra(data)

        return result

    # -------------------------------------------------
    # LOCATION
    # -------------------------------------------------

    def location(self, data):

        result = []

        scene = data.get("scene", {})

        location = scene.get("location")

        if location:
            result.append(location)

        return result

    # -------------------------------------------------
    # LIGHTING
    # -------------------------------------------------

    def lighting(self, data):

        result = []

        scene = data.get("scene", {})

        lighting = scene.get("lighting")

        if lighting:
            result.append(lighting)

        return result

    # -------------------------------------------------
    # TIME
    # -------------------------------------------------

    def time(self, data):

        result = []

        scene = data.get("scene", {})

        time = scene.get("time")

        if time:
            result.append(time)

        return result

    # -------------------------------------------------
    # WEATHER
    # -------------------------------------------------

    def weather(self, data):

        result = []

        scene = data.get("scene", {})

        weather = scene.get("weather")

        if weather:
            result.append(weather)

        return result

    # -------------------------------------------------
    # ATMOSPHERE
    # -------------------------------------------------

    def atmosphere(self, data):

        result = []

        scene = data.get("scene", {})

        atmosphere = scene.get("atmosphere")

        if atmosphere:
            result.append(atmosphere)

        return result

    # -------------------------------------------------
    # PROPS
    # -------------------------------------------------

    def props(self, data):

        result = []

        scene = data.get("scene", {})

        props = scene.get("props")

        if props:
            result.append(props)

        return result

    # -------------------------------------------------
    # EXTRA
    # -------------------------------------------------

    def extra(self, data):

        result = []

        scene = data.get("scene", {})

        extra = scene.get("extra")

        if extra:
            result.append(extra)

        return result
