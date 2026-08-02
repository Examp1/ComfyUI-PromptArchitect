from .character_prompt import CharacterPrompt
from .scene_prompt import ScenePrompt
from .appearance_prompt import AppearancePrompt

ASSEMBLERS = {
    "character": CharacterPrompt(),
    "scene": ScenePrompt(),
    "scene": AppearancePrompt(),
}