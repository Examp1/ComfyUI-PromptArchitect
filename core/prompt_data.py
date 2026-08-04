import ast
import copy


class PromptData:

    def __init__(self, data):

        if isinstance(data, str):
            data = ast.literal_eval(data)

        self.data = data

    # -------------------------------------------------

    def __repr__(self):

        return str(self.data)

    # -------------------------------------------------

    def __getitem__(self, key):

        return self.data[key]

    # -------------------------------------------------

    def raw(self):

        return self.data

    # -------------------------------------------------

    def serialize(self):

        return str(self.data)

    # -------------------------------------------------

    def clone(self):

        return PromptData(copy.deepcopy(self.data))

    # -------------------------------------------------

    def get(self, path, default=None):

        current = self.data

        for part in path.split("."):

            if not isinstance(current, dict):
                return default

            current = current.get(part)

            if current is None:
                return default

        return current

    # -------------------------------------------------

    def has(self, path):

        return self.get(path, None) is not None

    # -------------------------------------------------

    def set(self, path, value):

        current = self.data

        parts = path.split(".")

        for part in parts[:-1]:

            current = current.setdefault(part, {})

        current[parts[-1]] = value

    # -------------------------------------------------

    def update(self, path, value):

        self.set(path, value)

    # -------------------------------------------------

    def delete(self, path):

        current = self.data

        parts = path.split(".")

        for part in parts[:-1]:

            current = current.get(part)

            if current is None:
                return

        current.pop(parts[-1], None)

    # -------------------------------------------------

    def paths(self):

        result = []

        def walk(node, prefix=""):

            if not isinstance(node, dict):
                return

            for key, value in node.items():

                new_prefix = f"{prefix}.{key}" if prefix else key

                if isinstance(value, dict):

                    walk(value, new_prefix)

                else:

                    result.append(new_prefix)

        walk(self.data)

        return sorted(result)