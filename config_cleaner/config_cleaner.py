#!/usr/bin/env python3

"""
Clean up unused config files for uninstalled apps.
"""

import argparse
import os
import shutil
import sys
import warnings


def clean_up_configs(app_names: list[str], all: bool) -> None:
    """
    Clean up unused config files for uninstalled apps from the
    following directories:

    - ~/.cache/
    - ~/.config/
    - ~/.local/share/
    """

    if (home_directory := os.getenv("HOME")) is None:
        raise ValueError("Can't find your home directory.")

    # Convert strings to lowercase and remove empty strings
    app_names = [app_name.casefold() for app_name in app_names if app_name]

    config_directories = (
        os.path.join(home_directory, ".config"),
        os.path.join(home_directory, ".cache"),
        os.path.join(home_directory, ".local", "share"),
    )

    found_files = []

    # Search the config directories for specified config files
    for directory in config_directories:
        for app_name in app_names:
            try:
                for filename in os.listdir(directory):
                    if app_name in filename.casefold():
                        found_files.append(os.path.join(directory, filename))
            except OSError as e:
                warnings.warn(str(e))

    if found_files:
        # Because "1 files" looks a bit silly
        if len(found_files) > 1:
            print(f"Found {len(found_files)} files:\n")
        else:
            print("Found 1 file:\n")

        removed_count = 0
        kept_count = 0

        # Remove all files at once (optional), or one by one (default)
        if all:
            for file in found_files:
                print(f"- {file}")

            choice = input("\nRemove all of these files? [y/n] ").casefold()

            if choice.startswith("y"):
                print()

                for file in found_files:
                    try:
                        if os.path.isfile(file):
                            os.remove(file)
                        elif os.path.isdir(file):
                            shutil.rmtree(file)

                        removed_count += 1
                    except OSError as e:
                        warnings.warn(str(e))
                        kept_count += 1
                        continue

                    print(f"Removed {file}.")
            else:
                kept_count = len(found_files)
        else:
            try:
                for i, file in enumerate(found_files):
                    print(f"- {file}")
                    choice = input("Remove? [y/n] ").casefold()

                    if choice.startswith("y"):
                        try:
                            if os.path.isfile(file):
                                os.remove(file)
                            elif os.path.isdir(file):
                                shutil.rmtree(file)
                        except OSError as e:
                            warnings.warn(str(e))
                            kept_count += 1
                            continue

                        removed_count += 1

                        # Don't print a newline if it's the last in the list
                        if i == len(found_files) - 1:
                            print(f"Removed {file}.")
                        else:
                            print(f"Removed {file}.\n")
                    else:
                        kept_count += 1

                        # Again, print a newline if there's more in the list
                        if i != len(found_files) - 1:
                            print()
            except KeyboardInterrupt:
                kept_count = len(found_files) - removed_count
                print()

        if removed_count != 1:
            print(f"\nRemoved {removed_count} files; kept {kept_count}.")
        else:
            print(f"\nRemoved 1 file; kept {kept_count}.")
    else:
        print("No config files found.")


def main() -> None:
    """Main functionality of the script."""

    # Set up argparse
    parser = argparse.ArgumentParser(
        description="Clean up unused config files for uninstalled apps.",
        add_help=True,
    )

    parser.add_argument(
        "app_names",
        help="the name of the app whose config you want to remove",
        nargs="+",
        type=str,
        metavar="APP_NAME",
    )

    parser.add_argument(
        "-a",
        "--all",
        help="remove all files at once, rather than one by one",
        action="store_true",
    )

    # Show the help message and exit if no arguments are given
    args = parser.parse_args(sys.argv[1:] or ["-h"])

    clean_up_configs(args.app_names, args.all)


if __name__ == "__main__":
    main()
