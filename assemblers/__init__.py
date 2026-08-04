from .character_prompt import CharacterPrompt
from .scene_prompt import ScenePrompt
from .appearance_prompt import AppearancePrompt
from .camera_prompt import CameraPrompt
from .pose_prompt import PosePrompt

ASSEMBLERS = {

    "character": CharacterPrompt(),
    "appearance": AppearancePrompt(),
    "pose": PosePrompt(),
    "scene": ScenePrompt(),
    "camera": CameraPrompt(),

}