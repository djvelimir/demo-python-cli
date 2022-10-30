import sys

from dependency.container import Container
from program.program_base import ProgramBase


def main(args: list[str]) -> None:
    program: ProgramBase = Container.program()
    program.start(args)


if __name__ == '__main__':
    main(sys.argv)
