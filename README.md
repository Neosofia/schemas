# Schemas

Shared JSON schemas for service validation and documentation.

## Current versions

| Schema | File | Purpose |
|---|---|---|
| Log Entry | [`log-v1.0.0.json`](log-v1.0.0.json) | Structured log envelope |
| OpenAPI 3.0 | [`openapi-v3.0.json`](openapi-v3.0.json) | Validates OpenAPI 3.0.x specifications (vendored from the [OpenAPI Initiative](https://github.com/OAI/OpenAPI-Specification), Apache-2.0; see [NOTICE](NOTICE)) |

Schemas are immutable once published. New versions add a new file; old files are never edited.
Services pin by filename — bump the filename in your test to upgrade.

## Usage

```python
import json, pathlib, jsonschema, urllib.request

# Local (set SCHEMAS_DIR in .env):
schema = json.loads((pathlib.Path(schemas_dir) / "log-v1.0.0.json").read_text())

# Remote (CI default):
url = "https://raw.githubusercontent.com/neosofia/schemas/main/log-v1.0.0.json"
with urllib.request.urlopen(url) as r:
    schema = json.loads(r.read())

jsonschema.validate(log_entry, schema)
```

## Contributing

1. **Never edit a published `*-v*.json` file.** CI will block the PR.
2. To revise a schema, add a new file with a bumped version (e.g.
   `log-v1.1.0.json`) and update the table above.
3. Add example documents under `examples/<schema-stem>/`:
   - `valid-*.json` — must pass validation
   - `invalid-*.json` — must fail validation
4. CI runs on every PR:
   - Every `*.json` is checked as a valid JSON Schema (dialect auto-detected)
   - Every example is validated against its schema and asserted to behave as named
   - Modifications/deletions of existing `*-v*.json` files are blocked

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

## License

Apache-2.0 — see [LICENSE](LICENSE) and [NOTICE](NOTICE).

