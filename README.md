# Psychotherapy Skills Universal RU

Универсальная русскоязычная библиотека навыков для безопасной психологической поддержки в AI-системах.

## Состав репозитория

- 38 модульных навыков универсального пакета;
- отдельный self-skill для ChatGPT;
- кризисный роутер и ограничения безопасности;
- CBT, DBT, ACT, SFBT, narrative, schema-informed, IFS-informed и другие подходы;
- навыки для горя, травматической стабилизации, отношений, ADHD, зависимостей и сна;
- 20 тестовых сценариев;
- адаптеры для ChatGPT, Claude, Codex, Gemini и generic LLM;
- `research/` — каталог исходных GitHub-ресурсов.

> Это не медицинское устройство и не замена лицензированному психотерапевту, психиатру или экстренной помощи.


# Psychotherapy Skills Universal RU

Универсальный модульный пакет для Claude, Codex, ChatGPT, Gemini и локальных LLM.

## Внутри

- 38 файлов `SKILL.md`;
- роутер и governance;
- пять safety-модулей;
- разговорные навыки;
- CBT, DBT, ACT, SFBT, narrative, compassion-focused, schema, IFS, psychodynamic и existential;
- горе, травма-стабилизация, отношения, ADHD, зависимости, сон, подростки;
- micro-tools;
- адаптеры;
- 20 eval-сценариев;
- валидатор и сборщик system prompt.

## Проверка

```bash
python scripts/validate_package.py
```

## Сборка системного промпта

```bash
python scripts/build_prompt.py --skills 03-modalities/cbt/SKILL.md 05-tools/thought-record/SKILL.md
```

## Логика загрузки

Корневой SKILL → роутер → governance → crisis-triage → одна модальность → максимум один инструмент.

Это не медицинское изделие и не автономный психотерапевт. Пакет предназначен для поддержки, психообразования, саморефлексии и подготовки к живой помощи.
