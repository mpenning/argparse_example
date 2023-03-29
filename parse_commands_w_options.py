import shlex
import sys
import os

from argparse import ArgumentParser, FileType

"""
MIT License
https://opensource.org/licenses/MIT

Copyright 2023 David Michael Pennington

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

    ##########################################################################
    ##  - 1. Make a subparser for all commands
    cmds = parser.add_subparsers(dest="command", help="commands")
    
    ##########################################################################
    ##  - 2. Make a parser for the `cook` command and its argument groups
    cmds_cook = cmds.add_parser("cook", help="Cook something")

    ##########################################################################
    ##  - 2a.  Make required `cook` argument group
    cook_required_args = cmds_cook.add_argument_group("required")
    ##  - 2b.  Add an required `cook` '--recipe-book' filepath argument...
    cook_required_args.add_argument(
        "-r", "--recipe-book", required=True, type=FileType("w"), help="File path to the recipe book"
    )

    ##########################################################################
    ##  - 2c.  Make an optional `cook` argument group
    cook_optional_args = cmds_cook.add_argument_group("optional")
    ##         NOTE: Mutually exclusive args *must* be optional
    cook_exclusive_arg = cook_optional_args.add_mutually_exclusive_group()
    ##  - 2d.  Add an optional `cook` '--in-microwave' argument...
    cook_exclusive_arg.add_argument(
        "-m",
        "--in-microwave",
        action="store_true",
        default=False,
        required=False,
        help="cook in microwave",
    )
    ##  - 2e.  Add an optional `cook` '--on-stove' argument...
    cook_exclusive_arg.add_argument(
        "-s",
        "--on-stove",
        action="store_true",
        default=False,
        required=False,
        help="cook on the stove,
    )


    ##########################################################################
    ##  - 3. Build a parser for the `mix` command and its required arguments...
    cmds_mix = cmds.add_parser("mix", help="Mix something")
    ##  - 3a.  Make required `mix` arguments
    mix_required = cmds_mix.add_argument_group("required arguments")
    ##  - 3b.  Add a required `mix` argument...
    mix_required.add_argument(
        "-c",
        "--contents",
        help="Name of contents",
        action="store",
        required=True,
    )


    ##########################################################################
    ##  - 4. Build a parser for the `chop` command and its required arguments...
    chop = cmds.add_parser("chop", help="Chop something")
    ##  - 4a.  Make required `chop` arguments
    chop_required = chop.add_argument_group("required arguments")
    ##  - 4b.  Add a required `chop` argument...
    chop_required.add_argument(
        "-s",
        "--size",
        help="Chop to this size",
        action="store",
        type=float,
        required=True,
    )


    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()  # If parse_args() has no input string, then parse CLI
    fh = args.file  # Python file handle
    print args.command  # Prints the name of the command used
