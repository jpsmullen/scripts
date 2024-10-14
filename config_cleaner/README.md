# 🗑️ config cleaner

This script cleans up unused config files for uninstalled apps on Linux. It
scans the home directory, ~/.config/, ~/.cache/ and ~/.local/share/, and asks
for permission before removing anything.

## 🧑‍💻 usage

```
usage: config_cleaner.py [-h] [-a] APP_NAME [APP_NAME ...]

Clean up unused config files for uninstalled apps.

positional arguments:
  APP_NAME    the name of the app whose config you want to remove

options:
  -h, --help  show this help message and exit
  -a, --all   remove all files at once, rather than one by one
```

Removing files one by one:

```
$ python config_cleaner.py torbrowser akregator
Found 5 files:

- /home/joe/.config/torbrowser
Remove? [y/n] n

- /home/joe/.config/akregatorrc
Remove? [y/n] y
Removed /home/joe/.config/akregatorrc.

- /home/joe/.cache/torbrowser
Remove? [y/n] n

- /home/joe/.local/share/torbrowser
Remove? [y/n] n

- /home/joe/.local/share/akregator
Remove? [y/n] y
Removed /home/joe/.local/share/akregator.

Removed 2 files; kept 3.
```

Removing all files at once:

```
$ python config_cleaner.py torbrowser -a
Found 3 files:

- /home/joe/.config/torbrowser
- /home/joe/.cache/torbrowser
- /home/joe/.local/share/torbrowser

Remove all of these files? [y/n] y

Removed /home/joe/.config/torbrowser.
Removed /home/joe/.cache/torbrowser.
Removed /home/joe/.local/share/torbrowser.

Removed 3 files; kept 0.
```
