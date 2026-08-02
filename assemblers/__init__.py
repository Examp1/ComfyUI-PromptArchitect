from .character_prompt import CharacterPrompt
from .scene_prompt import ScenePrompt

ASSEMBLERS = {
    "character": CharacterPrompt(),
    "scene": ScenePrompt(),
}