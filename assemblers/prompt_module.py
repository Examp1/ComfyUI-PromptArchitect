class PromptModule:

    NAME = None
    RULES = {}

    # -------------------------------------------------

    def build(self, data):

        result = []

        for path, rule in self.RULES.items():

            value = self.get_value(data, path)

            if value is None:
                continue

            text = self.render(rule, value)

            if text:
                result.append(text)

        return result

    # -------------------------------------------------

    def get_value(self, data, path):

        current = data

        for part in path.split("."):

            if not isinstance(current, dict):
                return None

            current = current.get(part)

            if current is None:
                return None

        return current

    # -------------------------------------------------

    def render(self, rule, value):

        # ---------- normalize strings ----------

        if isinstance(value, str):

            value = value.strip()

            if not value:
                return None

            if value.lower() in (
                "none",
                "null",
            ):
                return None

        # ---------- callable ----------

        if callable(rule):

            text = rule(value)

            if not text:
                return None

            text = text.strip()

            if not text:
                return None

            return text

        # ---------- dict ----------

        if isinstance(rule, dict):

            return rule.get(value)

        # ---------- string template ----------

        if isinstance(value, str):

            text = rule.format(value=value).strip()

            if not text:
                return None

            return text

        return None