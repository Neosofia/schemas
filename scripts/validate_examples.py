"""Validate examples/<schema-stem>/{valid,invalid}-*.json against schemas.

Runs in CI. Exits non-zero if any example produces an unexpected result.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import validators
from jsonschema.exceptions import ValidationError

REPO = Path(__file__).resolve().parent.parent
EXAMPLES = REPO / "examples"


def main() -> int:
    failures: list[str] = []
    checked = 0

    for schema_path in sorted(REPO.glob("*-v*.json")):
        stem = schema_path.stem  # e.g. "log-v1.0.0"
        examples_dir = EXAMPLES / stem
        if not examples_dir.is_dir():
            failures.append(f"{stem}: no examples/ directory")
            continue

        schema = json.loads(schema_path.read_text())
        Validator = validators.validator_for(schema)
        validator = Validator(schema)

        for example in sorted(examples_dir.glob("*.json")):
            checked += 1
            doc = json.loads(example.read_text())
            errors = list(validator.iter_errors(doc))
            name = example.name

            if name.startswith("valid-") and errors:
                failures.append(
                    f"{stem}/{name}: expected VALID but got {len(errors)} error(s): "
                    f"{errors[0].message}"
                )
            elif name.startswith("invalid-") and not errors:
                failures.append(
                    f"{stem}/{name}: expected INVALID but validation passed"
                )
            elif not (name.startswith("valid-") or name.startswith("invalid-")):
                failures.append(
                    f"{stem}/{name}: filename must start with 'valid-' or 'invalid-'"
                )

    print(f"Checked {checked} example(s) across "
          f"{len(list(REPO.glob('*-v*.json')))} schema(s).")

    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f"  - {f}")
        return 1

    print("All examples behave as expected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
