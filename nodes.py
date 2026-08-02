from .character_builder import CharacterBuilder
from .prompt_assembler import PromptAssembler
from .scene_builder import SceneBuilder

NODE_CLASS_MAPPINGS = {

    "CharacterBuilder": CharacterBuilder,
    "PromptAssembler": PromptAssembler,
    "SceneBuilder": SceneBuilder,

}

NODE_DISPLAY_NAME_MAPPINGS = {

    "CharacterBuilder": "🧑 Character Builder",
    "PromptAssembler": "📝 Prompt Assembler",
    "SceneBuilder": "🎬 Scene Builder",

}