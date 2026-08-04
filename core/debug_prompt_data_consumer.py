class DebugPromptDataConsumer:

    CATEGORY = "Prompt Architect/Debug"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Output",)

    FUNCTION = "run"

    @classmethod
    def INPUT_TYPES(cls):

        return {

            "required": {

                "data": ("PROMPT_DATA",),

            }

        }

    def run(self, data):

        print("\n========== PROMPT DATA ==========\n")

        print(data)

        print("\n=================================\n")

        return ("OK",)