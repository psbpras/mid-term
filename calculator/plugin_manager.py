# calculator/plugin_manager.py
"""
Manages loading and executing plugins dynamically.
"""

import importlib
import os

class PluginManager:
    """Dynamically loads plugins from the 'plugins' directory."""

    @staticmethod
    def load_plugins():
        plugins = []
        plugin_dir = "plugins"
        for file in os.listdir(plugin_dir):
            if file.endswith(".py") and file != "__init__.py":
                module_name = f"plugins.{file[:-3]}"
                module = importlib.import_module(module_name)
                plugins.append(module)
        return plugins
