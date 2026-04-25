# Security Policy

## Reporting a Vulnerability

If you believe you have found a security vulnerability in any schema in this
repository (for example, a schema that fails to constrain sensitive fields,
or that could enable injection downstream), please report it privately.

**Email:** security@neosofia.com

Please include:
- The schema file and version (e.g. `log-v1.0.0.json`)
- A description of the issue and its potential impact
- A reproduction (a sample document that demonstrates the problem)

We will acknowledge receipt within 5 business days and aim to publish a
remediated schema (as a new version, per the immutability policy in the
README) within 30 days of confirmation.

## Scope

This repository contains JSON Schema definitions only. It contains no
executable code beyond a CI validation workflow. Vulnerabilities in
downstream services that *consume* these schemas should be reported to
those projects directly.
