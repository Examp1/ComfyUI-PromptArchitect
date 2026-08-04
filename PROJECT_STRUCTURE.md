# Prompt Architect

## Overview

Prompt Architect — это набор кастомных нод для ComfyUI, предназначенный для построения сложных промптов из независимых логических блоков.

Каждый блок отвечает только за одну область описания изображения.

Например:

- Character
- Appearance
- Pose
- Scene
- Camera

В дальнейшем можно добавить:

- Quality
- Lighting
- NSFW
- Emotions
- Actions
- Environment
- LoRA presets
- Style presets

Итоговый промпт собирается автоматически в правильном порядке.

---

# Project Structure

```
PromptArchitect/

│
├── nodes.py
│
├── prompt_assembler.py
│
├── builders/
│
│   └── generic_builder.py
│
├── schemas/
│
│   ├── character.py
│   ├── appearance.py
│   ├── pose.py
│   ├── scene.py
│   └── camera.py
│
├── assemblers/
│
│   ├── __init__.py
│   ├── prompt_module.py
│   ├── character_prompt.py
│   ├── appearance_prompt.py
│   ├── pose_prompt.py
│   ├── scene_prompt.py
│   └── camera_prompt.py
│
├── character_builder.py
├── appearance_builder.py
├── pose_builder.py
├── scene_builder.py
└── camera_builder.py
```

---

# Architecture

Работа проекта разделена на три уровня.

```
Schema
        ↓

Builder
        ↓

PromptModule
        ↓

PromptAssembler
```

---

# 1. Schema

Schemas описывают пользовательский интерфейс.

Например

```
schemas/character.py
```

описывает

- Gender
- Age
- Eyes
- Hair
- Body

Каждое поле автоматически появляется внутри ноды ComfyUI.

Schema НЕ содержит логики генерации промпта.

Она отвечает только за UI.

---

# 2. Builder

Builder превращает значения из UI в словарь.

Например

```
{
    "body": {
        "physique": "slim feminine",
        "figure": "hourglass"
    }
}
```

Builder ничего не знает о промптах.

Он только сериализует данные.

Все Builder используют

```
GenericBuilder
```

поэтому собственная логика практически никогда не нужна.

---

# 3. PromptModule

Каждая область имеет собственный PromptModule.

Например

```
CharacterPrompt
ScenePrompt
PosePrompt
```

Они превращают словарь Builder в список строк.

Например

```
"body.figure"
        ↓

hourglass figure
```

Вся логика генерации текста находится именно здесь.

---

# RULES

PromptModule использует словарь RULES.

Например

```
RULES = {

    "body.figure":
        "{value} figure",

    "body.physique":
        "{value} physique",

}
```

или

```
RULES = {

    "makeup.style": {

        "none": None,

        "light":
            "light makeup",

        "full glam":
            "full glam makeup",

    }

}
```

или

```
RULES = {

    "nails.style":

        lambda value:
            f"{value} nail polish"

}
```

PromptModule автоматически проходит по RULES и собирает итоговый текст.

---

# Prompt Assembler

PromptAssembler получает данные от всех Builder.

Например

```
CharacterBuilder

↓

AppearanceBuilder

↓

PoseBuilder

↓

SceneBuilder

↓

CameraBuilder
```

После чего вызывает соответствующие PromptModule.

Все строки объединяются в один итоговый промпт.

---

# Current Prompt Order

Порядок сборки промпта:

```
Character

↓

Appearance

↓

Pose

↓

Scene

↓

Camera
```

Между блоками автоматически вставляется пустая строка.

Это делает итоговый промпт читаемым.

---

# Adding New Node

Допустим необходимо добавить

```
Quality Builder
```

Последовательность действий всегда одинаковая.

---

## 1.

Создать схему

```
schemas/quality.py
```

---

## 2.

Создать Builder

```
quality_builder.py
```

```
from .builders.generic_builder import GenericBuilder
from .schemas.quality import SCHEMA


class QualityBuilder(GenericBuilder):

    SCHEMA = SCHEMA
```

---

## 3.

Создать PromptModule

```
assemblers/quality_prompt.py
```

```
from .prompt_module import PromptModule


class QualityPrompt(PromptModule):

    NAME = "quality"

    RULES = {

    }
```

---

## 4.

Зарегистрировать PromptModule

```
assemblers/__init__.py
```

```
ASSEMBLERS = {

    ...

    "quality":
        QualityPrompt(),

}
```

---

## 5.

Добавить Builder

```
nodes.py
```

в

```
NODE_CLASS_MAPPINGS
```

и

```
NODE_DISPLAY_NAME_MAPPINGS
```

---

## 6.

Подключить вход

```
prompt_assembler.py
```

```
optional={

    ...

    "quality":("STRING",),

}
```

и

```
GenericPrompt().assemble(

    ...

    quality=quality,

)
```

После этого новая нода полностью интегрирована.

---

# Design Principles

Проект строится по нескольким принципам.

## Single Responsibility

Каждая нода отвечает только за свою область.

Character не знает про одежду.

Appearance не знает про камеру.

Scene не знает про позу.

---

## Data Driven

Логика строится вокруг данных.

Builder создает словарь.

PromptModule преобразует словарь в текст.

Никакой логики внутри Builder нет.

---

## Easy Extensibility

Добавление новой ноды занимает несколько минут.

Никаких изменений ядра проекта обычно не требуется.

---

## Readable Prompt

Итоговый промпт должен быть таким, будто его написал человек вручную.

Например

```
young woman,
20-22 years old,
fair clear skin,
emerald green eyes

wearing white shirt,
full glam makeup

kneeling,
looking at camera

office,
soft lighting

professional portrait photograph,
shot on a 85mm lens
```

Это значительно упрощает отладку и дальнейшую работу.