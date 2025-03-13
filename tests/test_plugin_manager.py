# tests/test_plugin_manager.py

"""
Unit tests for the PluginManager class.
"""

import os
import pytest
from calculator.plugin_manager import PluginManager

@pytest.fixture
def create_test_plugin():
    """Creates a temporary test plugin file."""
    plugin_code = """
def test_function():
    return "Hello from Plugin"
"""
    os.makedirs("plugins", exist_ok=True)

    plugin_path = "plugins/test_plugin.py"
    with open(plugin_path, "w", encoding="utf-8") as f:  # Explicit encoding
        f.write(plugin_code)

    yield  # Fixture setup complete

    # Cleanup: Ensure file is removed safely
    if os.path.exists(plugin_path):
        os.remove(plugin_path)

@pytest.mark.usefixtures("create_test_plugin")  # Use fixture without explicit argument
def test_plugin_loading():
    """Test if the PluginManager correctly loads a plugin."""
    plugins = PluginManager.load_plugins()
    assert any(hasattr(plugin, "test_function") for plugin in plugins)
