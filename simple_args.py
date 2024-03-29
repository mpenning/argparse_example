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
    parse_required = parser.add_argument_group("required")
    parse_required.add_argument(
        "-f", "--file", required=True, type=FileType("w"), help="Foo file name"
    )  # required file in write mode

    parse_optional = parser.add_argument_group("optional")

    # Add a boolean flag to store_true...
    parse_optional.add_argument(
        "-m",
        "--my_flag",
        action="store_true",
        default=False,
        required=False,
        help="Enable my_flag argument",
    )

    ## Optional Argument with choices...
    parse_optional.add_argument(
        "-l",
        "--level",
        help="Foo file security level",
        action="store",
        type=str,
        required=False,
        choices=["public", "private"],
    )

    ## Exclusive optional arguments...
    parse_exclusive = parse_optional.add_mutually_exclusive_group()
    parse_exclusive.add_argument(
        "-b",
        "--bar",
        action="store_true",
        default=False,
        required=False,
        help="bar a created foo",
    )
    parse_exclusive.add_argument(
        "-z",
        "--baz",
        action="store_true",
        default=False,
        required=False,
        help="baz a created foo",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()  # If parse_args() has no input string, then parse CLI
