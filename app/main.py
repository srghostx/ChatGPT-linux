import os
import platform
from ai.OpenAI import OpenAI
from terminal.Terminal import Terminal

##change env

def main():
    try:

        ai = OpenAI()
        terminal = Terminal()

        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        exit_commands = terminal.get_exit_commands()
        while True:
            message = terminal.get_user_message()
            if message in exit_commands:
                break
            terminal.wait()
            response = ai.ask(message)
            terminal.stop_wait()
            terminal.display_response(response.message_raw)
    except OSError as e:
        pass


if __name__ == '__main__':
    main()
