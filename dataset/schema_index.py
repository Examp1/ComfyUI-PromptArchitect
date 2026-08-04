from .reflection import Reflection
from .schema_walker import SchemaWalker


class SchemaIndex:

    def __init__(self):

        self._index = {}

        reflection = Reflection()
        walker = SchemaWalker()

        for builder_name, builder in reflection.get_builders().items():

            fields = walker.walk(builder.SCHEMA)

            for field in fields:

                path = f"{builder_name}.{field['path']}"

                self._index[path] = field

    # -------------------------------------------------

    def get(self, path):

        return self._index.get(path)

    # -------------------------------------------------

    def keys(self):

        return self._index.keys()

    # -------------------------------------------------

    def values(self):

        return self._index.values()

    # -------------------------------------------------

    def items(self):

        return self._index.items()