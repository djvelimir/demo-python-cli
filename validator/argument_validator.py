from validator.argument_validator_base import ArgumentValidatorBase


class ArgumentValidator(ArgumentValidatorBase):
    def validate(self, argv: list[str]) -> bool:
        return len(argv) != 0 and len(argv) == 3 and argv[1] == 'generate' and argv[2] == 'password'
