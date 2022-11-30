import shlex
import sys
import os

from argparse import ArgumentParser, FileType

"""
MIT License
https://opensource.org/licenses/MIT

Copyright 2018 David Michael Pennington

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


def parse_args(input_str=""):
    """Parse CLI arguments, or parse args from the input_str variable"""

    ## input_str is useful if you don't want to parse args from the shell
    if input_str != "":
        # Example: parse_args("create -f this.txt -b")
        sys.argv = [input_str]  # sys.argv[0] is always the whole list of args
        sys.argv.extend(shlex.split(input_str))  # shlex adds the rest of argv

    parser = ArgumentParser(
        prog=os.path.basename(__file__),
        description="Help string placeholder",
        add_help=True,
    )

    ## Create a master subparser for all commands
    commands = parser.add_subparsers(help="commands", dest="command")

    ### Create a create command and its required and *optional* arguments...
    create = commands.add_parser("create", help="Create a foo")
    ## Make a required argument
    create_required = create.add_argument_group("required")
    create_required.add_argument(
        "-f", "--file", required=True, type=FileType("w"), help="Foo file name"
    )  # Write mode
    ## Make mutually exclusive optional arguments
    create_optional = create.add_argument_group("optional")
    ## NOTE: Mutually exclusive args *must* be optional
    create_exclusive = create_optional.add_mutually_exclusive_group()
    create_exclusive.add_argument(
        "-b",
        "--bar",
        action="store_true",
        default=False,
        required=False,
        help="bar a created foo",
    )
    create_exclusive.add_argument(
        "-z",
        "--baz",
        action="store_true",
        default=False,
        required=False,
        help="baz a created foo",
    )

    ### Create an append command and its arguments...
    append = commands.add_parser("append", help="Append a foo")
    append_required = append.add_argument_group("required arguments")
    append_required.add_argument(
        "-f",
        "--file",
        help="Foo file name",
        action="store",
        type=FileType("a"),
        required=True,
    )  # Append mode...

    ### Create an secure command and its arguments...
    secure = commands.add_parser("secure", help="Secure a foo")
    secure_required = secure.add_argument_group("required arguments")
    secure_required.add_argument(
        "-f",
        "--file",
        help="Foo file name",
        action="store",
        type=FileType("r"),
        required=True,
    )  # Read-only mode
    ## Multiple choices for secure 'level'
    secure_required.add_argument(
        "-l",
        "--level",
        help="Foo file security level",
        action="store",
        type=str,
        required=True,
        choices=["public", "private"],
    )

    ## Create an upload command, and its arguments...
    upload = commands.add_parser("upload", help="Upload a foo")
    upload.add_argument(
        "-f",
        "--file",
        required=True,
        default="",
        type=FileType("r"),
        help="foo file name",
    )  # Read-only mode

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()  # If parse_args() has no input string, then parse CLI
    fh = args.file  # Python file handle
    print args.command  # Prints the name of the command used

    try:
        print(args.level)  # Throws an error unless the command is 'secure'
    except AttributeError:
        pass
