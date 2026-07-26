---
name: behavioral-experiment
description: Проверяет предсказание небольшим безопасным экспериментом.
priority: P3
language: ru
portable: true
compatible_with: [claude, codex, chatgpt, gemini, llama, qwen, mistral, deepseek]
triggers:
  - "проверить убеждение"
  - "избегание"
exclusions:
  - "опасный эксперимент"
---

# Эксперимент

Предсказание → вероятность → минимальный безопасный тест → наблюдаемый результат → план остановки → вывод.

Нельзя проверять через провокацию агрессора, риск здоровью, нарушение закона или унижение.
