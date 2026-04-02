#!/bin/bash
echo "🌸 Starting Nightly Bloom Cycle..."
cocoon bloom --task "Optimize entire src/ directory" --generations 3 --mutation "deep_refactor"
echo "✅ Bloom cycle completed. DNA updated."
