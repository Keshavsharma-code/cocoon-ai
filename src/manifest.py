import json
from pathlib import Path
from dataclasses import asdict, field
from typing import Any, Dict, List, Optional
from cocoon.src.models.swarm import LarvaInfo, CocoonManifest

class ManifestHandler:
    def __init__(self, path: Path):
        self.path = path
        self.lock_path = path.with_suffix(".lock")

    def _acquire_lock(self):
        import time
        while self.lock_path.exists():
            time.sleep(0.1)
        self.lock_path.touch()

    def _release_lock(self):
        if self.lock_path.exists():
            self.lock_path.unlink()

    def load(self) -> CocoonManifest:
        if not self.path.exists():
            return CocoonManifest(project_name="cocoon_new")
        data = json.loads(self.path.read_text())
        larvae = [LarvaInfo(**l) for l in data.get("larvae", [])]
        return CocoonManifest(
            project_name=data.get("project_name", "cocoon_new"),
            version=data.get("version", "0.1.0"),
            larvae=larvae,
            state=data.get("state", "egg"),
            max_budget=data.get("max_budget", 5.0)
        )

    def save(self, manifest: CocoonManifest):
        self._acquire_lock()
        try:
            # Pydantic models use .model_dump() or .dict()
            data = manifest.model_dump()
            self.path.write_text(json.dumps(data, indent=2))
        finally:
            self._release_lock()

    def add_larva(self, larva: LarvaInfo):
        m = self.load()
        l_dict = asdict(larva)
        m.larvae.append(l_dict)
        self.save(m)

    def update_state(self, state: str):
        m = self.load()
        m.state = state
        self.save(m)
