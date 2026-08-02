import ast

from .character_prompt import CharacterPrompt


class GenericPrompt:

    def assemble(self, character):

        if isinstance(character, str):
            character = ast.literal_eval(character)

        prompt = []

        prompt += CharacterPrompt().build(character)

        return ",\n".join(prompt)