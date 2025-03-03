class PowerCommand:
    def execute(self, base, exponent):
        return base ** exponent

def register(invoker):
    invoker.register_command("power", PowerCommand().execute)
