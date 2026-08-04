import json

from ..assemblers import ASSEMBLERS


class PromptEngine:

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
                data = json.loads(data)

            block = assembler.build(data)

            if block:
                sections.append(",\n".join(block))

        quality = kwargs.get("quality")

        if quality:
            sections.append(quality.strip())

        return "\n\n".join(sections)