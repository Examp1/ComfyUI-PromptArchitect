# Prompt Architect

## Overview

Prompt Architect is a modular prompt-building framework for ComfyUI.

Each section of the final prompt is an independent module:

- Character
- Appearance
- Pose
- Scene
- Camera

Each module contains:

- its own UI Schema
- its own Builder
- its own Prompt Module

All modules are automatically combined into a single final prompt.

---

# Project Structure

```
PromptArchitect/

nodes.py

builders/
│
├── generic_builder.py
├── character_builder.py
├── appearance_builder.py
├── pose_builder.py
├── scene_builder.py
└── camera_builder.py

schemas/
│
├── character.py
├── appearance.py
├── pose.py
├── scene.py
└── camera.py

assemblers/
│
├── __init__.py
├── prompt_module.py
├── character_prompt.py
├── appearance_prompt.py
├── pose_prompt.py
├── scene_prompt.py
└── camera_prompt.py

core/
│
├── generic_prompt.py
└── prompt_assembler.py
```

---

# Architecture

```
Schema
   │
   ▼
Builder
   │
   ▼
Dictionary
   │
   ▼
PromptModule
   │
   ▼
PromptAssembler
   │
   ▼
Final Prompt
```

---

# Folder Description

## schemas/

Defines the node interface.

Schemas describe:

- Combo Boxes
- Text Fields
- Labels
- Available Values

Schemas only describe the UI and know nothing about prompt generation.

---

## builders/

Builders automatically generate the ComfyUI interface from a Schema.

They also serialize user input into a dictionary.

Example:

```python
{
    "hair": {
        "color": "copper red"
    }
}
```

Builders do **not** generate prompt text.

---

## assemblers/

Each Prompt Module is responsible for a single section of the final prompt.

Example:

### CharacterPrompt

↓

```
young woman,
emerald green eyes,
hourglass figure
```

### ScenePrompt

↓

```
studio,
golden hour lighting,
warm atmosphere
```

### CameraPrompt

↓

```
portrait photograph,
85mm lens,
sharp focus
```

Every Prompt Module is completely independent.

---

## core/

The core of the framework.

### generic_prompt.py

Runs every Prompt Module.

Collects all generated prompt fragments.

Merges them into a single list.

### prompt_assembler.py

Receives data from every Builder.

Passes it to GenericPrompt.

Returns the final prompt.

---

# PromptModule

Every Prompt Module inherits from `PromptModule`.

Example:

```python
from .prompt_module import PromptModule


class CharacterPrompt(PromptModule):

    NAME = "character"

    RULES = {

        "hair.color":
            "{value} hair",

        "body.figure":
            "{value} figure",

    }
```

RULES are automatically converted into prompt text.

Three rule types are supported.

---

## String Rule

```python
"{value} hair"
```

↓

```
red hair
```

---

## Dictionary Rule

```python
{
    "none": None,
    "light": "light makeup"
}
```

↓

```
light makeup
```

or nothing if the value maps to `None`.

---

## Lambda Rule

```python
lambda value: f"{value} nail polish"
```

↓

```
black nail polish
```

Use lambda functions whenever custom formatting is required.

---

# Builder

A Builder is intentionally minimal.

Example:

```python
from .generic_builder import GenericBuilder
from ..schemas.character import SCHEMA


class CharacterBuilder(GenericBuilder):

    SCHEMA = SCHEMA
```

`GenericBuilder` automatically creates the UI based on the provided Schema.

---

# Adding a New Builder

### 1. Create a Schema

```
schemas/example.py
```

---

### 2. Create a Builder

```
builders/example_builder.py
```

```python
class ExampleBuilder(GenericBuilder):

    SCHEMA = SCHEMA
```

---

### 3. Create a Prompt Module

```
assemblers/example_prompt.py
```

---

### 4. Register the Prompt Module

Edit:

```
assemblers/__init__.py
```

```python
ASSEMBLERS = {

    ...

    "example": ExamplePrompt(),

}
```

---

### 5. Register the Builder

Edit:

```
nodes.py
```

```python
NODE_CLASS_MAPPINGS = {

    ...

    "ExampleBuilder": ExampleBuilder,

}
```

---

### 6. Connect it to PromptAssembler

Add a new optional input:

```python
optional = {

    ...

    "example": ("STRING",),

}
```

The new module will now be automatically included in the final prompt.

---

# Design Philosophy

Each component has exactly one responsibility.

```
Schema
```

Defines the UI.

↓

```
Builder
```

Collects user input.

↓

```
PromptModule
```

Converts structured data into prompt text.

↓

```
PromptAssembler
```

Combines all modules into a single prompt.

This architecture keeps the system modular, scalable, and easy to extend. New modules can be added without modifying existing ones.