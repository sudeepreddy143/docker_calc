from app.commands.base import Command

class AddCommand(Command):
    def execute(self, a, b):
        return int(a) + int(b)

class SubtractCommand(Command):
    def execute(self, a, b):
        return int(a) - int(b)
