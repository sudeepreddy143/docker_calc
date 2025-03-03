class Command:
    """Base class for commands."""
    def execute(self, *args):
        raise NotImplementedError("Commands must implement execute() method")
