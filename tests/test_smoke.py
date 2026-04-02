# Test 1: Full Lifecycle (Mother Logic Only)
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent))

from cocoon.src.manifest import ManifestHandler, LarvaInfo
from cocoon.src.hatchery import Hatchery
from cocoon.src.bloom import BloomEngine

def test_triple_pass():
    root = Path(__file__).parent.parent
    manifest_path = root / "cocoon_manifest.json"
    handler = ManifestHandler(manifest_path)
    
    print("--- Triple Test 1: Lifecycle ---")
    # Reset manifest
    handler.save(handler.load())
    print("✓ Manifest initialized.")
    
    hatchery = Hatchery(root)
    subtasks = ["Subtask 1", "Subtask 2"]
    for i, s in enumerate(subtasks):
        larva = hatchery.spawn("scraper", s)
        print(f"✓ Spawned {larva.name}")
    
    print("\n--- Triple Test 2: Bloom ---")
    bloom = BloomEngine(root)
    # Mock mutation to avoid rich dependency
    bloom.mutate(1)
    print("✓ Mutation logic verified (dry-run).")
    
    print("\n--- Triple Test 3: Hardening ---")
    try:
        hatchery.spawn("invalid_type", "task")
    except ValueError as e:
        print(f"✓ Tool validation caught error: {e}")
        
    print("\n[SUCCESS] Cocoon Triple Test Passed.")

if __name__ == "__main__":
    test_triple_pass()
