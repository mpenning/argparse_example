
A quick example of python argparse usage...  this will allow you to use a command with specific options per command.

It requires the python `attrs` and `loguru` packages.

```python
from argparse import ArgumentParser, Namespace, FileType
from argparse import _SubParsersAction
from typing import List
import shlex
import sys
import os

from loguru import logger
import attrs


@attrs.define(repr=False)
class CLIParser:
    """
    :param input_str: String list of arguments
    :type input_str: str
    """
    input_str: str = ""

    argv: List = None
    parser: ArgumentParser = None
    subparsers: _SubParsersAction = None

    @logger.catch(reraise=True)
    def __init__(self, input_str: str = ""):
        if input_str == "":
            input_str = " ".join(sys.argv)

        self.input_str = input_str
        self.argv = [input_str]
        self.argv.extend(shlex.split(input_str))

        self.parser = None
        self.subparsers = None

        self.parser = ArgumentParser(
            prog=os.path.basename(__file__),
            description="Help string placeholder",
            add_help=True,
        )
        self.subparsers = self.parser.add_subparsers(help="commands", dest="command")

        self.build_command_project()
        self.build_command_task()

    def __repr__(self) -> str:
        return f"""<Parser '{" ".join(self.argv)}'>"""

    @logger.catch(reraise=True)
    def parse(self) -> Namespace:
        return self.parser.parse_args()

    @logger.catch(reraise=True)
    def build_command_project(self) -> None:
        """Build the project command as a subparser"""
        parser = self.subparsers.add_parser(
            "project",
            help="Create a new project")

        parser_required = parser.add_argument_group("required")
        parser_required.add_argument(
            "-p", "--project",
            required=True,
            type=str,
            help="Create a new project with this name")

        parser_optional = parser.add_argument_group("optional")
        parser_optional.add_argument(
            "-e", "--send_email",
            required=False,
            action='store_true',
            help="Send an email about the new project event")

        parser_optional_exclusive = parser_optional.add_mutually_exclusive_group()
        parser_optional_exclusive.add_argument(
            "-c", "--create",
            required=False,
            action='store_true',
            help="Create this new task")
        parser_optional_exclusive.add_argument(
            "-s", "--show",
            required=False,
            action='store_true',
            help="Show this new task")

    @logger.catch(reraise=True)
    def build_command_task(self) -> None:
        """Build the task command as a subparser"""
        parser = self.subparsers.add_parser(
            "task",
            help="Manage a task")

        parser_required = parser.add_argument_group("required")
        parser_required.add_argument(
            "-t", "--task",
            required=True,
            type=str,
            help="Task name")

        parser_optional = parser.add_argument_group("optional")
        parser_optional.add_argument(
            "-e", "--send_email",
            required=False,
            action='store_true',
            help="Send an email about the new task event")
        parser_optional.add_argument(
            "-o", "--owner",
            required=False,
            type=str,
            help="Set task owner")

        parser_optional_exclusive = parser_optional.add_mutually_exclusive_group()
        parser_optional_exclusive.add_argument(
            "-c", "--create",
            required=False,
            action='store_true',
            help="Create this new task")
        parser_optional_exclusive.add_argument(
            "-s", "--show",
            required=False,
            action='store_true',
            help="Show this new task")


if __name__=="__main__":
    parser = CLIParser()
    args = parser.parse()
    print(args)
```
