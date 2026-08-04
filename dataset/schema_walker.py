class SchemaWalker:

    def walk(self, schema):

        fields = []

        for section in schema:

            section_id = section["id"]

            for field in section["fields"]:

                fields.append({

                    "path": f"{section_id}.{field['id']}",

                    "label": field.get("label", field["id"]),

                    "type": field.get("type"),

                    "values": field.get("values", []),

                })

        return fields