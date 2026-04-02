#!/bin/bash
echo "🦋 Installing Cocoon: The Infinite Agent Swarm..."

# Verify if we are in the project root
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Please run this command from the 'cocoon' project directory."
    exit 1
fi

# Install the package in editable mode
python3 -m pip install -e . --user

# Detect pip bin directory
PIP_BIN=$(python3 -m site --user-base)/bin
if [[ ":$PATH:" != *":$PIP_BIN:"* ]]; then
    echo "⚠️  Warning: $PIP_BIN is not in your PATH."
    echo "Add it by running: echo 'export PATH=\"$PIP_BIN:\$PATH\"' >> ~/.zshrc && source ~/.zshrc"
fi

echo "✅ Cocoon Installed!"
echo "Run 'cocoon --help' to start."
