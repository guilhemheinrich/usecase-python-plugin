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

### Option 2: Using Poetry

If you prefer Poetry, rename the files:

```bash
# In each directory (core, plugin, final):
mv pyproject.toml pyproject-setuptools.toml
mv pyproject-poetry.toml pyproject.toml
```

Then install:

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
