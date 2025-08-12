#!/bin/bash

# Setup script for the devcontainer
echo "🚀 Setting up Python Plugin System project..."

# Add Poetry to PATH for current session
export PATH="$HOME/.local/bin:$PATH"

# Install packages in correct order
echo "📦 Installing core package..."
cd core && poetry install && cd ..

echo "🔌 Installing plugin package..."
cd plugin && poetry install && cd ..

echo "🎯 Installing final demo package..."
cd final && poetry install && cd ..

echo "✅ Setup complete! You can now run:"
echo "   cd final && poetry run python test_demo.py"
