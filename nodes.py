from .character_builder import CharacterBuilder
from .prompt_assembler import PromptAssembler
from .scene_builder import SceneBuilder
from .appearance_builder import AppearanceBuilder
from .camera_builder import CameraBuilder

NODE_CLASS_MAPPINGS = {

    "CharacterBuilder": CharacterBuilder,
    "PromptAssembler": PromptAssembler,
    "SceneBuilder": SceneBuilder,
    "AppearanceBuilder": AppearanceBuilder,
    "CameraBuilder": CameraBuilder,

}

NODE_DISPLAY_NAME_MAPPINGS = {

    "CharacterBuilder": "🧑 Character Builder",
    "PromptAssembler": "📝 Prompt Assembler",
    "SceneBuilder": "🎬 Scene Builder",
    "AppearanceBuilder": "👗 Appearance Builder",
    "CameraBuilder": "📷 Camera Builder",
}