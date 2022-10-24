from display.terminal_base import TerminalBase


class Terminal(TerminalBase):
    def show(self, message: str) -> None:
        print(message)
