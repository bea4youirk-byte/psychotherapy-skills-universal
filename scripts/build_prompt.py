from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
default = [
    "SKILL.md",
    "00-router/SKILL.md",
    "00-governance/scope-boundaries/SKILL.md",
    "01-safety/crisis-triage/SKILL.md",
    "02-core/reflective-listening/SKILL.md",
]
parser = argparse.ArgumentParser()
parser.add_argument("--skills", nargs="*", default=[])
parser.add_argument("--output", default="dist/combined_system_prompt.md")
args = parser.parse_args()

chunks, seen = [], set()
for rel in default + args.skills:
    if rel in seen:
        continue
    seen.add(rel)
    p = ROOT/rel
    if not p.exists():
        raise SystemExit(f"Нет файла: {rel}")
    chunks.append(f"\n\n<!-- SOURCE: {rel} -->\n\n" + p.read_text(encoding="utf-8"))

out = ROOT/args.output
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("".join(chunks), encoding="utf-8")
print(out)
