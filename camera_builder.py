from .builders.generic_builder import GenericBuilder
from .schemas.camera import SCHEMA


class CameraBuilder(GenericBuilder):
    SCHEMA = SCHEMA