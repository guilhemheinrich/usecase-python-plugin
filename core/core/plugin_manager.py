"""Plugin manager for discovering and listing plugins via entrypoints."""

import importlib.metadata
from typing import Callable, Dict, List


def list_plugins() -> List[str]:
    """
    Discover and return list of plugin function names from entrypoints.

    Returns:
        List of plugin function names available through entrypoints
    """
    plugin_names = []

    try:
        # Discover all entrypoints in the 'core.plugins' group
        entrypoints = importlib.metadata.entry_points(group="core.plugins")

        for entrypoint in entrypoints:
            plugin_names.append(entrypoint.name)

    except Exception as e:
        print(f"Error discovering plugins: {e}")

    return plugin_names


def get_plugin_functions() -> Dict[str, Callable]:
    """
    Load and return plugin functions from entrypoints.

    Returns:
        Dictionary mapping plugin names to their loaded functions
    """
    plugins = {}

    try:
        # Discover all entrypoints in the 'core.plugins' group
        entrypoints = importlib.metadata.entry_points(group="core.plugins")

        for entrypoint in entrypoints:
            try:
                # Load the function from the entrypoint
                plugin_func = entrypoint.load()
                plugins[entrypoint.name] = plugin_func
            except Exception as e:
                print(f"Error loading plugin '{entrypoint.name}': {e}")

    except Exception as e:
        print(f"Error discovering plugins: {e}")

    return plugins
