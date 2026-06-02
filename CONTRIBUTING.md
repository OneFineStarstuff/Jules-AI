# Contributing to Sovereign AI Governance Suite

First off, thank you for considering contributing to the Sovereign AI Governance Suite! It's people like you that make it a premier tool for high-assurance AGI governance.

## Our Standards

This repository handles high-stakes, civilizational-scale safety protocols. As such, we maintain extremely high engineering standards:

1.  **High-Assurance Code:** All core governance kernels (GDL Compiler, IRMI Driver) require 100% unit test coverage and formal verification using TLA+.
2.  **Protocol Compliance:** All inter-service communication MUST use gRPC with mTLS. SPIFFE IDs are mandatory.
3.  **Privacy First:** Never log PII. Use the provided `hash_pii()` utility for any sensitive identifiers.
4.  **Governance Registration:** Every new API endpoint MUST be registered with the Sentinel v2.4 Sidecar for GDL policy enforcement.

## How Can I Contribute?

### Reporting Bugs

Bugs are tracked as GitHub issues. When creating a bug report, please include as much detail as possible, including:
- A clear, descriptive title.
- Steps to reproduce the bug.
- Expected vs actual behavior.
- Environment details (OS, version of the suite, etc.).

### Suggesting Enhancements

We welcome suggestions for new features and improvements. Please open an issue to discuss your ideas before starting work.

### Pull Requests

1.  Fork the repository and create your branch from `main`.
2.  Ensure your code adheres to the existing style and standards.
3.  Include tests for any new functionality.
4.  Update documentation as necessary.
5.  All PRs must pass the CI/CD pipeline, including formal verification checks.

## Style Guide

- Follow PEP 8 for Python code.
- Follow the Google JavaScript Style Guide for Node.js components.
- Use meaningful variable names and include comments for complex logic.

## Security

If you discover a security vulnerability, please do NOT open an issue. Instead, follow our security policy (if available) or email the maintainers directly at security@agent.com.

---

**Sovereign Authority Jules**
