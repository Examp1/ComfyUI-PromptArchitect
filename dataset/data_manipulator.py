class DataManipulator:

    # ----------------------------------------

    def get(self, data, path):

        current = data

        for part in path.split("."):

            if not isinstance(current, dict):
                return None

            current = current.get(part)

            if current is None:
                return None

        return current

    # ----------------------------------------

    def set(self, data, path, value):

        current = data

        parts = path.split(".")

        for part in parts[:-1]:

            current = current.setdefault(part, {})

        current[parts[-1]] = value

        return data