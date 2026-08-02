import ast

from . import ASSEMBLERS


class GenericPrompt:

    def assemble(self, **kwargs):

        prompt = []

        for name, assembler in ASSEMBLERS.items():

            data = kwargs.get(name)

            if not data:
                continue

            if isinstance(data, str):
                data = ast.literal_eval(data)

            prompt += assembler.build(data)

        return ",\n".join(prompt)