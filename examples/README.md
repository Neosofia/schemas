# Schema Examples

Each schema has a corresponding directory of example documents:
- `valid-*.json` — documents that MUST pass validation
- `invalid-*.json` — documents that MUST fail validation

The CI workflow asserts both conditions on every push. These files double as
documentation: they show consumers what the schema accepts and rejects.
