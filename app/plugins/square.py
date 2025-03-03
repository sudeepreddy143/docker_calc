class SquareCommand:
    def execute(self, number):
        return number * number

def register(invoker):
    invoker.register_command("square", SquareCommand().execute)
