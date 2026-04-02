# 🐣 Hatching Custom Larvae

Cocoon is designed for extensibility. You can build specialized agents for any domain by following the `Larva` interface.

## 1. Inherit from BaseLarva
Create a new file in `src/larvae/my_agent.py`:

```python
from cocoon.src.larvae import BaseLarva

class MySpecialist(BaseLarva):
    def execute(self) -> str:
        # Define logic here
        return "Result from specialized work"
```

## 2. Register in the Hatchery
Update `src/hatchery.py` to recognize your new species.

## 3. Deployment
The Mother agent will now be able to spawn `MySpecialist` whenever a task description matches its domain.
