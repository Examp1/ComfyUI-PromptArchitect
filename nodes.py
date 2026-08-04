from .builders.character_builder import CharacterBuilder
from .core.prompt_assembler import PromptAssembler
from .builders.scene_builder import SceneBuilder
from .builders.appearance_builder import AppearanceBuilder
from .builders.camera_builder import CameraBuilder
from .builders.pose_builder import PoseBuilder
from .dataset.dataset_generator import DatasetGenerator

NODE_CLASS_MAPPINGS = {

    "CharacterBuilder": CharacterBuilder,
    "PromptAssembler": PromptAssembler,
    "SceneBuilder": SceneBuilder,
    "AppearanceBuilder": AppearanceBuilder,
    "CameraBuilder": CameraBuilder,
    "PoseBuilder": PoseBuilder,
    "DatasetGenerator": DatasetGenerator,

}

NODE_DISPLAY_NAME_MAPPINGS = {

    "CharacterBuilder": "🧑 Character Builder",
    "PromptAssembler": "📝 Prompt Assembler",
    "SceneBuilder": "🎬 Scene Builder",
    "AppearanceBuilder": "👗 Appearance Builder",
    "CameraBuilder": "📷 Camera Builder",
    "PoseBuilder": "🧍 Pose Builder",
    "DatasetGenerator": "🧍 📚 Dataset Generator",
}