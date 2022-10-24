from src.validator.argument_validator_base import ArgumentValidatorBase


class ArgumentValidator(ArgumentValidatorBase):
    def validate(self, args: list[str]) -> bool:
        return len(args) != 0 and len(args) == 3 and args[1] == 'generate' and args[2] == 'password'
