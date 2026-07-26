from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
skills = list(ROOT.rglob("SKILL.md"))
required = ["name:", "description:", "priority:", "triggers:", "exclusions:"]

for p in skills:
    text = p.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"{p.relative_to(ROOT)}: нет frontmatter")
    for key in required:
        if key not in text[:1800]:
            errors.append(f"{p.relative_to(ROOT)}: нет {key}")

for rel in ["SKILL.md","00-router/SKILL.md","01-safety/crisis-triage/SKILL.md","06-evaluation/test_cases.jsonl"]:
    if not (ROOT/rel).exists():
        errors.append(f"нет обязательного файла {rel}")

for i, line in enumerate((ROOT/"06-evaluation/test_cases.jsonl").read_text(encoding="utf-8").splitlines(), 1):
    try:
        obj = json.loads(line)
        for k in ("id","input","expected_route","must","must_not"):
            if k not in obj:
                errors.append(f"тест {i}: нет {k}")
    except Exception as e:
        errors.append(f"тест {i}: {e}")

if errors:
    print("FAIL")
    print("\n".join("- " + e for e in errors))
    sys.exit(1)

print(f"OK: {len(skills)} SKILL.md; структура и JSONL валидны")
