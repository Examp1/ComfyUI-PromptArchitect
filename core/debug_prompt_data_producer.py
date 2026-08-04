class DebugPromptDataProducer:

    CATEGORY = "Prompt Architect/Debug"

    RETURN_TYPES = ("PROMPT_DATA",)
    RETURN_NAMES = ("Data",)

    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):

        return {
            "required": {}
        }

    def run(self):

        data = {

            "test": {
                "name": "Alice",
                "age": 20
            }

        }

        return (data,)