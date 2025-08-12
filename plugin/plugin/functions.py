"""Plugin functions exposed via entrypoints."""


def hello_world() -> str:
    """
    Simple hello world function for plugin demonstration.
    
    Returns:
        Hello world message
    """
    return "Hello World from plugin!"
