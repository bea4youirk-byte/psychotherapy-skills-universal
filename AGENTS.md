# Codex / ChatGPT repository operating rules

Preserve user privacy, confidentiality, existing project instructions and all source files. Do not commit sensitive personal information, client records, credentials or secrets.

## MANDATORY — safe change gate for existing or live systems (2026-11-19)

This repository follows the global production-change policy: https://github.com/bea4youirk-byte/codex-os-private/blob/main/policies/production-change-gate.md .

If the task touches an existing website, application, user-facing system, database, automation or connected app: production is READ-ONLY by default; inventory actual existing/latest local work, verify a recoverable files-and-data backup, verify an isolated copy with live external side effects disabled, and implement/test ONLY in that copy. Review evidence and obtain user acceptance, then require a separate explicit user instruction for any production deployment. "Finish the stage" and access credentials are NOT deployment permissions. Any unknown execution environment is a hard stop. If unintended live edits are suspected, stop writes and preserve evidence; never auto-roll back an entire site/database or overwrite unrelated recent user records.

Preserve all stricter medical/privacy and repository-specific restrictions. Documentation updates do not authorize any live integrations or content publication.
