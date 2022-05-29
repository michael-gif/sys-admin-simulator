class CommandManager:
    def __init__(self):
        self.commands = {}

    def add_command(self, keyword, callback):
        self.commands[keyword] = callback

    def execute(self, keyword, args):
        if keyword in self.commands:
            self.commands[keyword](args)


command_manager = CommandManager()
