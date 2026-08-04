class GenericBuilder:

    SCHEMA = []

    CATEGORY = "Prompt Architect"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Data",)

    FUNCTION = "build"

    # -------------------------------------------------
    # Extension points
    # -------------------------------------------------

    EXTRA_INPUTS = {}

    # -------------------------------------------------

    @classmethod
    def INPUT_TYPES(cls):

        required = {}

        # ==========================================================
        # EXTRA INPUTS
        # ==========================================================

        required.update(cls.EXTRA_INPUTS)

        # ==========================================================
        # SCHEMA
        # ==========================================================

        for group in cls.SCHEMA:

            group_prefix = group["id"]

            if group_prefix == "eyes":
                group_prefix = "eye"

            for field in group["fields"]:

                widget_name = f"{group_prefix}_{field['id']}"

                field_type = field["type"]

                # ----------------------------------------------

                if field_type == "combo":

                    required[widget_name] = (
                        field["values"],
                    )

                # ----------------------------------------------

                elif field_type == "string":

                    required[widget_name] = (
                        "STRING",
                        {
                            "default": "",
                            "multiline": False,
                        },
                    )

                # ----------------------------------------------

                elif field_type == "multiline":

                    required[widget_name] = (
                        "STRING",
                        {
                            "default": "",
                            "multiline": True,
                        },
                    )

        return {

            "required": required

        }

    # -------------------------------------------------

    def build(self, **kwargs):

        data = {}

        # ==========================================================

        for group in self.SCHEMA:

            group_id = group["id"]

            group_prefix = group_id

            if group_prefix == "eyes":
                group_prefix = "eye"

            data[group_id] = {}

            for field in group["fields"]:

                widget_name = f"{group_prefix}_{field['id']}"

                data[group_id][field["id"]] = kwargs[widget_name]

        # ==========================================================
        # Allow child builders to modify output
        # ==========================================================

        self.after_build(

            data,

            kwargs,

        )

        return (

            str(data),

        )

    # -------------------------------------------------

    def after_build(

        self,

        data,

        kwargs,

    ):

        """
        Override in child builders.

        Modify `data` before it is returned.
        """

        pass