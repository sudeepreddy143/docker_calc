import importlib
import pkgutil
import logging
from app.database import Database

class Invoker:
    def __init__(self):
        self.commands = {}
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Invoker initialized")
        self.db = Database()  # Initialize database
        self._register_builtin_commands()
        self._register_plugins()

    def register_command(self, name, command):
        """Register a new command."""
        self.commands[name] = command
        self.logger.info(f"Registered command → {name}")

    def execute_command(self, name, *args):
        """Execute a registered command and log it to the database."""
        if name in self.commands:
            self.logger.info(f"Executing command → {name} with args {args}")
            result = self.commands[name](*args)
            self.db.log_command(name, str(args), str(result))  # Log in DB
            return result

        self.logger.warning(f"Unknown command: {name}")
        return "Result: Unknown command."

    def _register_builtin_commands(self):
        """Register built-in commands like add, subtract."""
        from app.commands.basic import AddCommand, SubtractCommand
        self.register_command("add", AddCommand().execute)
        self.register_command("subtract", SubtractCommand().execute)

    def _register_plugins(self):
        """Dynamically load all plugins from the plugins directory."""
        try:
            import app.plugins  # Ensure package is accessible
            package = app.plugins
            self.logger.debug(f"Checking plugins in: {package.__path__}")

            for _, modname, _ in pkgutil.iter_modules(package.__path__):
                self.logger.debug(f"Found plugin: {modname}")
                module = importlib.import_module(f"app.plugins.{modname}")
                if hasattr(module, "register"):
                    module.register(self)
                    self.logger.info(f"Loaded plugin: {modname}")
                else:
                    self.logger.warning(f"Plugin {modname} has no 'register' function.")
        except Exception as e:
            self.logger.error(f"Error loading plugins: {e}")
