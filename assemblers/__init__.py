from .character_prompt import CharacterPrompt
from .scene_prompt import ScenePrompt
from .appearance_prompt import AppearancePrompt
from .camera_prompt import CameraPrompt

ASSEMBLERS = {
    "character": CharacterPrompt(),
    "scene": ScenePrompt(),
    "appearance": AppearancePrompt(),
    "camera": CameraPrompt(),
}