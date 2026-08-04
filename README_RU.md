# Prompt Architect

## Overview

Prompt Architect — это модульная система построения промптов для ComfyUI.

Каждая часть промпта является независимым модулем:

- Character
- Appearance
- Pose
- Scene
- Camera

Каждый модуль имеет:

- собственную схему UI
- собственный Builder
- собственный Prompt Module

Все они автоматически объединяются в один финальный промпт.

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

Описывает интерфейс ноды.

Здесь находятся:

- Combo Box
- Text Fields
- Labels
- Values

Schema ничего не знает о генерации промпта.

---

## builders/

Builder автоматически строит UI по Schema.

Также Builder сериализует введённые пользователем данные в Dictionary.

Например:

```python
{
    "hair": {
        "color": "copper red"
    }
}
```

Builder не занимается генерацией текста.

---

## assemblers/

Каждый PromptModule отвечает только за один раздел промпта.

Например:

CharacterPrompt

↓

```
young woman,
emerald green eyes,
hourglass figure
```

ScenePrompt

↓

```
studio,
golden hour lighting,
warm atmosphere
```

CameraPrompt

↓

```
portrait photograph,
85mm lens,
sharp focus
```

Каждый PromptModule полностью независим.

---

## core/

Ядро всей системы.

### generic_prompt.py

Проходит по всем PromptModule.

Получает их результат.

Объединяет их в список.

### prompt_assembler.py

Получает данные со всех Builder.

Передаёт их в GenericPrompt.

Возвращает финальный prompt.

---

# PromptModule

Все PromptModule наследуются от PromptModule.

Пример:

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

RULES автоматически преобразуются в текст.

Можно использовать:

### String

```python
"{value} hair"
```

↓

```
red hair
```

---

### Dictionary

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

или ничего.

---

### Lambda

```python
lambda value: f"{value} nail polish"
```

↓

```
black nail polish
```

---

# Builder

Каждый Builder состоит всего из нескольких строк.

Пример:

```python
from .generic_builder import GenericBuilder
from ..schemas.character import SCHEMA


class CharacterBuilder(GenericBuilder):

    SCHEMA = SCHEMA
```

GenericBuilder самостоятельно строит интерфейс.

---

# Adding New Builder

1.

Создать новую Schema.

```
schemas/example.py
```

---

2.

Создать Builder.

```
builders/example_builder.py
```

```python
class ExampleBuilder(GenericBuilder):

    SCHEMA = SCHEMA
```

---

3.

Создать PromptModule.

```
assemblers/example_prompt.py
```

---

4.

Добавить PromptModule в

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

5.

Добавить Builder в

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

6.

Подключить Builder в PromptAssembler.

```
optional={
    "example": ("STRING",),
}
```

После этого новый модуль автоматически станет частью финального промпта.

---

# Philosophy

Каждый модуль отвечает только за одну задачу.

Schema

↓

описывает интерфейс.

Builder

↓

получает данные.

PromptModule

↓

превращает данные в текст.

PromptAssembler

↓

объединяет всё вместе.

Благодаря этому можно легко добавлять новые разделы без изменения существующего кода.