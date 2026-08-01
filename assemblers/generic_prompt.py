import ast


class GenericPrompt:

    def __init__(self, schema):
        self.schema = schema

    def assemble(self, data):

        if isinstance(data, str):
            data = ast.literal_eval(data)

        prompt = []

        for group in self.schema:

            group_id = group["id"]

            if group_id not in data:
                continue

            group_values = data[group_id]

            for field in group["fields"]:

                field_id = field["id"]

                value = group_values.get(field_id)

                if value in (None, "", "None"):
                    continue

                template = field.get("prompt")

                if template:

                    prompt.append(
                        template.format(value=value)
                    )

        return ",\n".join(prompt)