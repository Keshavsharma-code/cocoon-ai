# Cocoon Architecture: Brain & Muscle

Cocoon leverages a dual-language architecture to provide the best of both worlds: high-level reasoning and high-performance execution.

## The Brain (Python - Mother Agent)
Relying on Python's rich ecosystem and the `claw-code` patterns:
- **LLM Reasoning**: Intent parsing and task decomposition.
- **TUI Dashboard**: Rich visual feedback.
- **Guardrails**: Budgeting and Human-in-the-Loop logic.

## The Muscle (Rust - Chrysalis Runtime)
Built for speed and safety:
- **Concurrent I/O**: High-speed file operations.
- **Sandboxed Execution**: Safe execution of terminal commands.
- **MCP Implementation**: Standardized tool connections.
- **Nectar API**: Fast, streaming access to multi-provider LLMs.
