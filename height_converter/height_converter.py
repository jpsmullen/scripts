#!/usr/bin/env python3

"""
Simple script for converting heights in cm to feet and inches.
"""

import argparse
import sys


def cm_to_ft_in(
    cm_height: float,
    rounding: int | None,
) -> tuple[int, int | float]:
    """Convert centimetres to feet and inches."""

    # 1 inch == 2.54cm
    total_inches = cm_height / 2.54

    # 1 foot == 12 inches
    feet = int(total_inches / 12)

    if rounding is not None:
        inches = round(total_inches % 12, rounding)
    else:
        inches = total_inches % 12

    # Fix things like 5'12" instead of 6'0"
    if inches == 12:
        feet += 1
        inches = 0

    # e.g. return 3 instead of 3.0
    inches = int(inches) if inches.is_integer() else inches

    return feet, inches


def main() -> None:
    """Main functionality of the script."""

    # Set up argparse
    parser = argparse.ArgumentParser(
        description="Convert heights from cm to feet and inches.",
        add_help=True,
    )

    parser.add_argument(
        "heights",
        help="heights in cm (e.g. 182, 160, 180.5, 172.75)",
        nargs="+",
        type=float,
        metavar="CM_HEIGHTS",
    )

    parser.add_argument(
        "-r",
        "--round",
        help="round the result to X decimal places (default: 0)",
        nargs="?",
        type=int,
        const=0,
        metavar="X",
    )

    # Show the help message and exit if no arguments are given
    args = parser.parse_args(sys.argv[1:] or ["-h"])

    for cm_height in args.heights:
        feet, inches = cm_to_ft_in(cm_height, args.round)

        # e.g. print 172 instead of 172.0
        cm_height = int(cm_height) if cm_height.is_integer() else cm_height

        if args.round is not None:
            print(f"{cm_height}cm is roughly {feet}'{inches}\"")
        else:
            print(f"{cm_height}cm is approximately {feet}'{inches}\"")


if __name__ == "__main__":
    main()
