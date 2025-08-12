"""Core plugin system module."""

from .plugin_manager import list_plugins, get_plugin_functions
from .animal import Animal
from .animals_manager import discover_animals, make_all_sounds

__all__ = ['list_plugins', 'get_plugin_functions',
           'Animal', 'discover_animals', 'make_all_sounds']
