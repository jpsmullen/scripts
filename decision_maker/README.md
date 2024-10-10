# 🎲 decision maker

This is a very simple script that reads lines from the user and chooses a random
one; useful if you have multiple options for something and want to make a
decision. It's basically [easydecisionmaker.com](https://easydecisionmaker.com/),
except it works offline and in your terminal.

## 🧑‍💻 usage

Let's say you don't know what to make for dinner. You run the script, enter your
choices and hit Ctrl+D when finished, and the script decides for you.

```
$ perl decision_maker.pl
carbonara
katsu curry
stir fry
==============================
katsu curry
==============================
```

You can also pipe the output of other programs into this script (e.g. `cat`),
but I'm not sure why you'd want to:

```
$ cat ../LICENCE | perl decision_maker.pl
==============================
(if any) on which the executable work runs, or a compiler used to
==============================
```
