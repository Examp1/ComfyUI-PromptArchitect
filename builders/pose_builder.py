from ..core.generic_builder import GenericBuilder
from ..schemas.pose import SCHEMA


class PoseBuilder(GenericBuilder):

    CATEGORY = "Prompt Architect"

    SCHEMA = SCHEMA

    # Эта информация понадобится JS
    NODE_SCHEMA = SCHEMA