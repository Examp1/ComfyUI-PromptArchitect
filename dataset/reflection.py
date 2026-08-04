from ..builders.character_builder import CharacterBuilder
from ..builders.appearance_builder import AppearanceBuilder
from ..builders.pose_builder import PoseBuilder
from ..builders.scene_builder import SceneBuilder
from ..builders.camera_builder import CameraBuilder


class Reflection:

    def get_builders(self):

        return {

            "character": CharacterBuilder,
            "appearance": AppearanceBuilder,
            "pose": PoseBuilder,
            "scene": SceneBuilder,
            "camera": CameraBuilder,

        }