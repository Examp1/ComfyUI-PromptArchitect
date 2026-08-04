import ast

from . import ASSEMBLERS


class GenericPrompt:

    def assemble(self, **kwargs):

        sections = []

        order = [
            "character",
            "appearance",
            "pose",
            "scene",
            "camera",
        ]

        for name in order:

            assembler = ASSEMBLERS.get(name)

            if assembler is None:
                continue

            data = kwargs.get(name)

            if not data:
                continue

            if isinstance(data, str):
                data = ast.literal_eval(data)

            block = assembler.build(data)

            if block:

                sections.append(",\n".join(block))

        return "\n\n".join(sections)
