"""A statement printer taking 2 variables. Made to make sure Python files work
fine, without any input lag, on Neovim. This also checks for any linter errors,
as well as checking the effect on Vim that autocompleters have when enabled."""

from decimal import Decimal

STATEMENT_ONE = "Hello, world! Here's a decimal!"
DECIMAL_ONE = Decimal('10.85')


def statement_printer(part1, part2):
    """Prints 2 chosen statements"""
    return print(part1 + part2)


statement_printer(STATEMENT_ONE, DECIMAL_ONE)
