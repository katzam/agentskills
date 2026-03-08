# Reasoning Certificate

Use this only for analysis-heavy, execution-free, or high-risk claims.

Keep it short.

## Template

```md
## Reasoning Certificate
Question: <what is being established>
Relevant files: <files inspected>
Dependencies: <key symbols, callers, callees, data contracts>
Execution path: <runtime or control-flow path being reasoned about>
Premises:
- <fact from code or docs>
- <fact from code or docs>
Conclusion: <claim supported by the premises>
Validated by: <commands run, or "static analysis only">
Confidence: <low|medium|high>
```

Do not use this for routine implementation steps when direct execution or tests provide stronger evidence.

