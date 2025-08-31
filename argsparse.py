"""
A description of the script.

Example:

    python script.py \
            --arg1 string
            --arg2 int
            --arg3 float
            --argflag
"""

import sys
from argparse import ArgumentParser


def add_args(parser):
    """
    Adds command-line arguments to parser

    Returns:
        argparse.Namespace: the parsed arguments
    """
    parser.add_argument(
        "--arg1",
        default="String",
        type=str,
        help="A string argument.",
    )
    parser.add_argument(
        "--arg2",
        default=None,
        type=int,
        help="An integer argument.",
    )
    parser.add_argument(
        "--arg3",
        default=1.312,
        type=float,
        help="A float argument",
    )
    parser.add_argument(
        "--argflag",
        default=False,
        action="store_true",
        help="A flag argument. False by default. True if passed.",
    )
    return parser


def print_args(args):
    """
    Prints the arguments

    Parameters
    ----------
    args : argparse.Namespace
        The parsed arguments
    """
    print("Arguments:")
    darg = vars(args)
    max_k = max([len(k) for k in darg]) + 1
    for k in darg:
        print(f"\t{k:{max_k}}: {darg[k]}")


def main(args):
    """
    Main method of the script.

    Parameters
    ----------
    args : argparse.Namespace
        The parsed arguments
    """
    print_args(args)


if __name__ == "__main__":
    parser = ArgumentParser()
    _, override_args = parser.parse_known_args()
    parser = add_args(parser)
    args = parser.parse_args()
    main(args)
    sys.exit()
