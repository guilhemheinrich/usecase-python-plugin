"""Demo script showing plugin system in action."""

from core import list_plugins, get_plugin_functions


def run_demo():
    """
    Demonstrate the plugin system by listing and executing plugins.
    """
    print("=== Plugin System Demo ===")
    
    # List available plugin names
    plugin_names = list_plugins()
    print(f"Available plugins: {plugin_names}")
    
    # Get plugin functions
    plugin_functions = get_plugin_functions()
    print(f"Loaded {len(plugin_functions)} plugin(s)")
    
    # Execute each plugin function
    for name, func in plugin_functions.items():
        try:
            result = func()
            print(f"Plugin '{name}' result: {result}")
        except Exception as e:
            print(f"Error executing plugin '{name}': {e}")


if __name__ == "__main__":
    run_demo()
