from .builders.generic_builder import GenericBuilder
from .schemas.pose import SCHEMA


class PoseBuilder(GenericBuilder):
    SCHEMA = SCHEMA