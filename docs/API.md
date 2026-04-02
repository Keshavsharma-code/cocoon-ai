# 🔗 Cocoon Programmatic API

Inject the power of the swarm directly into your own applications.

## Quick Start (Python)

```python
from cocoon.src.mother import cli
from cocoon.src.hatchery import Hatchery

# 1. Initialize a swarm
hatchery = Hatchery(Path("./my_swarm"))
decomposition = hatchery.decompose_goal("Build a bot")

# 2. Spawn and execute
# ...
```

The API allows for custom orchestration logic, bypassing the CLI for automated integrations.
