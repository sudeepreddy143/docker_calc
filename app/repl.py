import logging
from app.invoker import Invoker

def start_repl():
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)
    
    invoker = Invoker()
    logger.debug(f"Final registered commands → {list(invoker.commands.keys())}")

    print("Welcome to the interactive calculator! Type 'exit' to quit.")
    
    while True:
        try:
            command = input("> ").strip()
            if command.lower() == "exit":
                print("Exiting...")
                break
            elif command.lower() == "menu":
                logger.info("User requested the menu.")
                commands_list = ', '.join(invoker.commands.keys())
                logger.debug(f"Available commands: {commands_list}")
                print(f"Available commands: {commands_list}")
            elif command.lower() == "history":
                logger.info("User requested command history.")
                history = invoker.db.get_history(10)
                if history:
                    print("Command History:")
                    for cmd, args, result, timestamp in history:
                        print(f"[{timestamp}] {cmd} {args} → {result}")
                else:
                    print("No history available.")
            else:
                parts = command.split()
                cmd_name, args = parts[0], map(int, parts[1:])
                result = invoker.execute_command(cmd_name, *args)
                print(f"Result: {result}")
        except Exception as e:
            logger.error(f"Error: {e}")

if __name__ == "__main__":
    start_repl()
