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

        if callable(rule):

            text = rule(value)

            return text if text else None

        if isinstance(rule, dict):

            return rule.get(value)

        if isinstance(value, str):

            return rule.format(value=value)

        return None