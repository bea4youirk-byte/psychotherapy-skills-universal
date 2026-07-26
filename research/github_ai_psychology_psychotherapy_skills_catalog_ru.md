# GitHub-каталог AI-skills по психологии, психотерапии и эмоциональной поддержке

**Дата среза:** 26 июля 2026 года  
**Формат:** отобранные репозитории, skill-банки, отдельные skills, бенчмарки, датасеты и инженерные референсы.

> Важно: буквального конечного списка «всех» репозиториев не существует — GitHub меняется ежедневно, а названия `AI therapist` часто скрывают учебные чат-боты. Каталог ориентирован на повторно используемые skills и крупные источники, а не на каждую копию одного и того же демо.

## Что брать в основу

1. **Mental Wellness Prompts** — базовые границы, безопасный разговор, кризисные маршруты и provider-neutral инструкции.
2. **Satori** — глубокая рефлексия: MI, IFS, DBT, CFT, schema/somatic и ценностная работа.
3. **AutoSkill Psychology SkillBank** — 111 техник в пяти школах; главный сырьевой банк для отбора.
4. **OpenClaw Medical Skills** — отдельные модули кризиса, горя, ADHD, зависимостей, сна и модерации.
5. **CounselBench + AnnoMI** — обязательная проверка качества и MI-поведения.
6. **EmoLLM** — инженерный стек для локальных/дообучаемых моделей.

## Крупнейший профильный банк: AutoSkill

| Школа | Количество | Содержание |
|---|---:|---|
| [Гуманистически-экзистенциальная школа](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E4%BA%BA%E6%9C%AC-%E5%AD%98%E5%9C%A8%E4%B8%BB%E4%B9%89/%E6%80%BB%E6%8A%80%E8%83%BD) | 6 | Эмпатическое присутствие, гештальт/пустой стул, экзистенциальная работа и переживание опыта. |
| [Постмодернистские подходы](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E5%90%8E%E7%8E%B0%E4%BB%A3%E4%B8%BB%E4%B9%89/%E6%80%BB%E6%8A%80%E8%83%BD) | 9 | SFBT, нарративные и деконструктивные техники, экстернализация, работа с исключениями. |
| [Психодинамическая школа](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E5%BF%83%E7%90%86%E5%8A%A8%E5%8A%9B%E5%AD%A6/%E6%80%BB%E6%8A%80%E8%83%BD) | 17 | Перенос/контрперенос, символизация, работа со сновидениями, защитами, отношениями и кризисной формулировкой. |
| [Поведенческая школа](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E8%A1%8C%E4%B8%BA%E4%B8%BB%E4%B9%89/%E6%80%BB%E6%8A%80%E8%83%BD) | 11 | Экспозиция, систематическая десенсибилизация, поведенческая активация, подкрепление и формирование поведения. |
| [Когнитивно-поведенческая школа](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E8%AE%A4%E7%9F%A5%E8%A1%8C%E4%B8%BA%E7%96%97%E6%B3%95/%E6%80%BB%E6%8A%80%E8%83%BD) | 68 | CBT, REBT/ABC, ACT, когнитивная концептуализация, реструктуризация, поведенческие эксперименты, mindfulness и домашние задания. |

**Всего: 111 skills.** Внутри каждого дерева есть `SKILL.md`, `children_map.md`, `children_manifest.json` и evidence-материалы. Это удобно для машинного импорта, перевода и дедупликации.

## Полный отобранный каталог

| Приоритет | Категория | Название | Зрелость | Ключевая оговорка |
|---|---|---|---|---|
| A | Базовый терапевтический каркас | [Mental Wellness Prompts](https://github.com/joebwd/mental-wellness-prompts) | Высокая для open-source prompt framework | Хорошие границы, но не медицинское изделие и не замена специалиста |
| A- | Глубокая рефлексия и поддержка | [Satori](https://github.com/MetcalfSolutions/Satori) | Средне-высокая | Есть явные ограничения роли; авторский, не клинически сертифицированный продукт |
| A- | Крупнейший профильный skill-bank | [AutoSkill — Psychology Counseling SkillBank](https://github.com/ECNU-ICALK/AutoSkill) | Исследовательская, активно развивается | Не считать автоматически клинически валидированным; часть навыков требует перевода, дедупликации и экспертного аудита |
| A-/B+ | AutoSkill: школа психотерапии | [Гуманистически-экзистенциальная школа — 6 навыков](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E4%BA%BA%E6%9C%AC-%E5%AD%98%E5%9C%A8%E4%B8%BB%E4%B9%89/%E6%80%BB%E6%8A%80%E8%83%BD) | Исследовательская | Нужен клинический и культурный аудит; часть материалов на китайском |
| A-/B+ | AutoSkill: школа психотерапии | [Постмодернистские подходы — 9 навыков](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E5%90%8E%E7%8E%B0%E4%BB%A3%E4%B8%BB%E4%B9%89/%E6%80%BB%E6%8A%80%E8%83%BD) | Исследовательская | Нужен клинический и культурный аудит; часть материалов на китайском |
| A-/B+ | AutoSkill: школа психотерапии | [Психодинамическая школа — 17 навыков](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E5%BF%83%E7%90%86%E5%8A%A8%E5%8A%9B%E5%AD%A6/%E6%80%BB%E6%8A%80%E8%83%BD) | Исследовательская | Нужен клинический и культурный аудит; часть материалов на китайском |
| A-/B+ | AutoSkill: школа психотерапии | [Поведенческая школа — 11 навыков](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E8%A1%8C%E4%B8%BA%E4%B8%BB%E4%B9%89/%E6%80%BB%E6%8A%80%E8%83%BD) | Исследовательская | Нужен клинический и культурный аудит; часть материалов на китайском |
| A-/B+ | AutoSkill: школа психотерапии | [Когнитивно-поведенческая школа — 68 навыков](https://github.com/ECNU-ICALK/AutoSkill/tree/main/SkillBank/DocSkill/%E5%BF%83%E7%90%86%E5%92%A8%E8%AF%A2/Family%E6%8A%80%E8%83%BD/%E8%AE%A4%E7%9F%A5%E8%A1%8C%E4%B8%BA%E7%96%97%E6%B3%95/%E6%80%BB%E6%8A%80%E8%83%BD) | Исследовательская | Нужен клинический и культурный аудит; часть материалов на китайском |
| B | OpenClaw: Кризисная безопасность | [crisis-detection-intervention-ai](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/crisis-detection-intervention-ai) | Смешанная; библиотечный модуль | США-центричные ресурсы и неподтверждённые метрики; требуется локализация и red-team. |
| B | OpenClaw: Кризисная безопасность | [crisis-response-protocol](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/crisis-response-protocol) | Смешанная; библиотечный модуль | Использовать только как шаблон; юридические и страновые правила менять. |
| B | OpenClaw: Приватность и комплаенс | [hipaa-compliance](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/hipaa-compliance) | Смешанная; библиотечный модуль | HIPAA не покрывает GDPR/РФ/другие юрисдикции. |
| B | OpenClaw: Клиническое мышление | [clinical-diagnostic-reasoning](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/clinical-diagnostic-reasoning) | Смешанная; библиотечный модуль | Не выдавать пользователю диагноз; лучше как инструмент специалиста. |
| B- | OpenClaw: Аналитика состояния | [mental-health-analyzer](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/mental-health-analyzer) | Смешанная; библиотечный модуль | Высокий риск ложной уверенности и псевдодиагностики. |
| B | OpenClaw: Сон и поведение | [sleep-analyzer](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/sleep-analyzer) | Смешанная; библиотечный модуль | Не заменяет сомнолога и медицинскую диагностику. |
| B+ | OpenClaw: Цели и коучинг | [goal-analyzer](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/goal-analyzer) | Смешанная; библиотечный модуль | Относительно низкий риск при чётком разграничении с терапией. |
| B- | OpenClaw: Семейный контекст | [family-health-analyzer](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/family-health-analyzer) | Смешанная; библиотечный модуль | Особая осторожность с приватностью членов семьи. |
| B | OpenClaw: Эмоциональная осознанность | [hrv-alexithymia-expert](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/hrv-alexithymia-expert) | Смешанная; библиотечный модуль | Не делать медицинских выводов только по HRV. |
| B+ | OpenClaw: ADHD и исполнительные функции | [adhd-daily-planner](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/adhd-daily-planner) | Смешанная; библиотечный модуль | Поддержка быта, не диагностика и не лечение ADHD. |
| B+ | OpenClaw: Горе и утрата | [grief-companion](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/grief-companion) | Смешанная; библиотечный модуль | Нужен кризисный роутинг и запрет навязывать стадии горя. |
| B- | OpenClaw: Юнгианский подход | [jungian-psychologist](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/jungian-psychologist) | Смешанная; библиотечный модуль | Только рефлексивный/символический режим; не выдавать интерпретацию за факт. |
| B | OpenClaw: Зависимости | [modern-drug-rehab-computer](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/modern-drug-rehab-computer) | Смешанная; библиотечный модуль | Высокий риск: лечение, детокс и лекарства — только через клинициста. |
| B+ | OpenClaw: Сообщества восстановления | [recovery-community-moderator](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/recovery-community-moderator) | Смешанная; библиотечный модуль | Нужны прозрачные правила модерации и человеческая эскалация. |
| B | OpenClaw: Смежная помощь | [speech-pathology-ai](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/tree/main/skills/speech-pathology-ai) | Смешанная; библиотечный модуль | Клиническая оценка остаётся у специалиста. |
| B+ | Создание и эволюция skills | [AutoSkill engine](https://github.com/ECNU-ICALK/AutoSkill) | Активный исследовательский проект | Самоэволюция без human review опасна в психологии |
| B | Реестр skills | [Claude Skill Registry — clinical foundations](https://github.com/majiayu000/claude-skill-registry) | Большой агрегатор | Качество неоднородно, возможны дубликаты и зеркала |
| B- | Прототип master-skill | [Psychotherapy Counseling Master](https://github.com/swaylq/master-skill/tree/main/prototypes/psychotherapy-counseling-master) | Прототип | Не считать готовым терапевтическим продуктом |
| B- | Прототип master-skill | [Youth Mental Health Education Master](https://github.com/swaylq/master-skill/tree/main/prototypes/youth-mental-health-edu-master) | Прототип | Работа с несовершеннолетними требует повышенных ограничений и родительских/профессиональных маршрутов |
| B- | ADHD/CBT skill | [health-adhd-cbt](https://github.com/mjcramerz/codex-manager/tree/main/resources/plugins/skills/health-adhd-cbt) | Экспериментальная | Требуется содержательный аудит |
| B | Психологическое интервьюирование | [Elicitation](https://github.com/BehiSecc/awesome-claude-skills) | Индекс | Риск скрытого профилирования; необходимо согласие пользователя |
| B- | Психообразование | [mental_health_psychoeducation](https://github.com/AtifAssari/MCP-Skills-Universe/blob/master/skills_library/batch_17/mental_health_psychoeducation.md) | Низко-средняя | Автоматическая агрегация; качество и происхождение проверять |
| B+ | Дообучение модели | [Fine-Tuning Preparation / therapy domain](https://github.com/mattnigh/skills_collection/blob/main/collection/marcgreen__therapy-coach-finetune__claude__skills__finetune-prep__SKILL.md) | Средняя | Опасно заменять реальных клиницистов LLM-roleplay; нужен экспертный контроль |
| B | Дообучение эмоционального компаньона | [Fumii Fine-Tuning Skill](https://github.com/Mrun25/Hearth_Emotional-Companion/blob/main/docs/HEARTH_FINETUNE_SKILL.md) | Экспериментальная | Некоторые правила запрещают стандартные safety-фразы; кризисный слой должен иметь приоритет |
| A | Бенчмарк безопасности и качества | [CounselBench](https://github.com/llm-eval-mental-health/CounselBench) | Высокая исследовательская ценность | Бенчмарк не доказывает клиническую эффективность продукта |
| A- | Датасет Motivational Interviewing | [AnnoMI](https://github.com/uccollab/AnnoMI) | Исследовательский датасет | Проверить лицензию и допустимое использование |
| B+ | Модельный стек mental-health LLM | [EmoLLM](https://github.com/SmartFlowAI/EmoLLM) | Исследовательская | Качество зависит от корпуса и языка; клиническая валидация отдельно |
| B- | Учебный fine-tuning | [MentalHealthAssistant](https://github.com/Cody-Lange/MentalHealthAssistant) | Учебная | CounselChat не равен клинически валидированным сессиям; старое семейство модели |
| B- | Локальный приватный прототип | [SafeSpace](https://github.com/danlou/safespace) | Прототип | Синтетические Rogerian-транскрипты и Reddit-источники ограничивают надёжность |
| C+ | Приложение-референс | [AI Therapist](https://github.com/neilgebhard/ai-therapist) | Прототип | Наличие UI не означает терапевтическую безопасность |
| B- | CBT UX-референс | [Quirk](https://github.com/Flaque/quirk) | Зрелый UX-референс | Не является AI therapy skill |
| B- | Каталог ресурсов | [Awesome Mental Health](https://github.com/dreamingechoes/awesome-mental-health) | Каталог | Не терапевтический skill |
| C/D | Не брать без полного аудита | [Mental-health-Chatbot](https://github.com/Rogendo/Mental-health-Chatbot) | Низкая/неясная | Нет достаточных доказательств безопасности и клинической пригодности |
| C/D | Не брать без полного аудита | [Chatbot-for-mental-health](https://github.com/pandeyanuradha/Chatbot-for-mental-health) | Низкая/неясная | Нет достаточных доказательств безопасности и клинической пригодности |
| C/D | Не брать без полного аудита | [mental-health-chatbot](https://github.com/kairess/mental-health-chatbot) | Низкая/неясная | Нет достаточных доказательств безопасности и клинической пригодности |
| C/D | Не брать без полного аудита | [RASA-Mental-Health-Chatbot](https://github.com/stutisehgal/RASA-Mental-Health-Chatbot) | Низкая/неясная | Нет достаточных доказательств безопасности и клинической пригодности |
| C/D | Не брать без полного аудита | [Mental-Health-ChatBot](https://github.com/Huzaib/Mental-Health-ChatBot) | Низкая/неясная | Нет достаточных доказательств безопасности и клинической пригодности |
| C/D | Не брать без полного аудита | [Emotionally-Intelligent-Chatbot-for-Mental-Healthcare-and-suicide-prevention](https://github.com/varrhythm/Emotionally-Intelligent-Chatbot-for-Mental-Healthcare-and-suicide-prevention) | Низкая/неясная | Нет достаточных доказательств безопасности и клинической пригодности |

## Архитектура универсального пакета для любых моделей

```text
psychotherapy-skills-universal/
├── 00-governance/
│   ├── scope-and-boundaries.md
│   ├── informed-consent.md
│   ├── privacy-and-memory.md
│   └── minors-and-vulnerable-users.md
├── 01-safety/
│   ├── crisis-detection.md
│   ├── crisis-response-and-human-escalation.md
│   ├── self-harm-and-suicide.md
│   ├── abuse-and-domestic-violence.md
│   └── psychosis-mania-intoxication-red-flags.md
├── 02-core-conversation/
│   ├── empathy-without-false-claims.md
│   ├── reflective-listening.md
│   ├── motivational-interviewing.md
│   ├── intake-and-goal-contract.md
│   └── session-closing.md
├── 03-modalities/
│   ├── cbt/
│   ├── dbt/
│   ├── act/
│   ├── solution-focused/
│   ├── narrative/
│   ├── schema/
│   ├── ifs-informed/
│   ├── compassion-focused/
│   ├── psychodynamic-reflection/
│   └── existential-humanistic/
├── 04-life-situations/
│   ├── grief/
│   ├── relationships/
│   ├── trauma-informed-stabilization/
│   ├── adhd-executive-function/
│   ├── sleep/
│   ├── addiction-recovery/
│   └── parenting-and-adolescents/
├── 05-tools/
│   ├── thought-records/
│   ├── behavioral-experiments/
│   ├── grounding/
│   ├── emotion-regulation/
│   └── values-and-action/
└── 06-evaluation/
    ├── CounselBench-adapter/
    ├── AnnoMI-adapter/
    ├── crisis-red-team/
    ├── cultural-bias-tests/
    └── regression-tests/
```

### Почему не один огромный «психотерапевт-промпт»

- Модальности конфликтуют: например, когнитивное оспаривание не всегда уместно при остром горе или диссоциации.
- Кризисный и юридический слой должен иметь приоритет над стилем и терапевтической техникой.
- Роутер должен выбирать одну основную технику и максимум один поддерживающий micro-skill.
- Все интерпретации должны маркироваться как гипотезы, а не как диагнозы или факты о человеке.

## Переносимость между моделями

| Среда | Как подключать |
|---|---|
| Claude / Claude Code | Папка skill + `SKILL.md`; references рядом; при необходимости plugin manifest. |
| Codex | `.codex/skills/<skill-name>/SKILL.md` или инструкции проекта/AGENTS.md; убрать Claude-specific tool syntax. |
| ChatGPT | Project instructions / custom GPT knowledge / отдельные markdown-модули; tool calls описывать заново под доступные действия. |
| Gemini | System instructions/Gem; markdown-контент переносим, function calling и память адаптируются отдельно. |
| Llama/Qwen/Mistral/DeepSeek | System prompt + RAG/skill router; длинные reference-файлы хранить вне промпта и подгружать по запросу. |
| OpenClaw/NanoClaw | Нативный `SKILL.md`; проверять `allowed-tools`, внешние команды и permissions. |

## Жёсткие фильтры перед установкой

1. Нет кризисной эскалации и правил для самоповреждения — **не устанавливать**.
2. Обещает диагноз, лечение, замену психотерапевта или гарантированный результат — **отбраковать**.
3. Использует личные данные без явного согласия и срока хранения — **отбраковать**.
4. Автоматически интерпретирует травму, сновидения, личность или отношения как факт — **ограничить рефлексивным режимом**.
5. Навязывает одну школу всем пользователям — **разделить на роутер и узкие skills**.
6. Не имеет eval-набора и regression-тестов — **не выпускать в production**.

## Итоговая сборка, которую имеет смысл делать

**База:** Mental Wellness Prompts  
**Глубина:** Satori  
**Техники:** отобранные и переведённые skills из AutoSkill  
**Специализации:** OpenClaw grief / ADHD / addiction / recovery moderation  
**Безопасность:** собственный локализованный кризисный пакет с human escalation  
**Оценка:** CounselBench + AnnoMI + отдельный red-team на суицид, насилие, психоз, манию, несовершеннолетних и зависимость  
**Инженерия:** EmoLLM или provider-neutral RAG/router  

## Примечание о качестве

GitHub-звёзды, красивый интерфейс и слово `therapist` в названии не являются клинической валидацией. Даже сильные репозитории здесь нужно рассматривать как исходные материалы для безопасного помощника, психообразования, подготовки к сессии или поддержки между сессиями — не как автономного лицензированного психотерапевта.