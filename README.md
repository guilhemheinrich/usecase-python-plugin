# Python Plugin System Demo

This project demonstrates how to use Python entrypoints to create a plugin system with three packages:

## Project Structure

- **core/**: Core plugin system that discovers plugins via entrypoints
- **plugin/**: Example plugin with a `hello_world` function
- **final/**: Demo application that uses the core system and loads plugins

## Installation

### Option 1: Using pip (recommended for testing)

```bash
# Install core package
pip install -e core/

# Install plugin package  
pip install -e plugin/

# Install final demo package
pip install -e final/
```

### Option 2: Using Poetry (modern PEP 621 syntax)

The pyproject.toml files now use the modern PEP 621 syntax which works with both setuptools and Poetry:

```bash
# Install core package
cd core/
poetry install
cd ..

# Install plugin package
cd plugin/ 
poetry install
cd ..

# Install final demo package
cd final/
poetry install
```

Note: Requires Python >=3.9 for full PEP 621 support.

### Option 3: Using DevContainer

If you use VS Code or GitHub Codespaces, you can use the provided devcontainer:

1. Open the project in VS Code
2. When prompted, click "Reopen in Container"
3. Once the container is built, run the setup script:
   ```bash
   ./.devcontainer/setup.sh
   ```

The devcontainer includes Python 3.10, pip, and Poetry pre-configured.

## Usage

After installation, run the demo:

```bash
cd final/
python test_demo.py
```

Expected output:
```
=== Plugin System Demo ===
Available plugins: ['hello_world']
Loaded 1 plugin(s)
Plugin 'hello_world' result: Hello World from plugin!
```

## How It Works

1. The **core** package defines an entrypoint group `core.plugins`
2. The **plugin** package registers its `hello_world` function in this group
3. The **final** package uses the core system to discover and execute plugins

The magic happens through Python's `importlib.metadata.entry_points()` which automatically discovers registered plugins.
