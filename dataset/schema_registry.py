from builders.character_builder import CharacterBuilder
from builders.appearance_builder import AppearanceBuilder
from builders.pose_builder import PoseBuilder
from builders.scene_builder import SceneBuilder
from builders.camera_builder import CameraBuilder

REGISTRY = {

    "CharacterBuilder": CharacterBuilder.SCHEMA,
    "AppearanceBuilder": AppearanceBuilder.SCHEMA,
    "PoseBuilder": PoseBuilder.SCHEMA,
    "SceneBuilder": SceneBuilder.SCHEMA,
    "CameraBuilder": CameraBuilder.SCHEMA,

}