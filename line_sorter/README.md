# 🔢 line sorter

This script takes a list of lines as input, either directly from the user or
from a list of files, and sorts these lines in alphabetical order. The sorting is
case-insensitive, and blank lines are ignored.

## 🧑‍💻 usage

If no files are specified, input will be taken directly from the user. Enter
your lines and press Ctrl+D when you're done.

This is useful if you, for example, are organising your room and want to sort
the games or books on your shelf in alphabetical order.

```shell
$ perl line_sorter.pl
metal gear solid v: the phantom pain
batman: arkham knight
infamous: second son
uncharted 4: a thief's end
sleeping dogs: definitive edition
==================================================
1. batman: arkham knight
2. infamous: second son
3. metal gear solid v: the phantom pain
4. sleeping dogs: definitive edition
5. uncharted 4: a thief's end
==================================================
```

Sorting lines from a list of files (note that the case doesn't matter):

```shell
$ perl line_sorter.pl games.txt movies.txt
==================== games.txt ====================
1. batman: arkham knight
2. infamous: second son
3. metal gear solid v: the phantom pain
4. sleeping dogs: definitive edition
5. uncharted 4: a thief's end
==================== movies.txt ====================
1. lost in translation
2. submarine
3. the batman
4. The Big Lebowski
5. the incredibles
6. your name
==================================================
```

Sorting the output of other programs piped into this script (note the lack of
blank lines, and that this is a stupid example):

```shell
$ python -m this | perl line_sorter.pl
==================================================
1. Although never is often better than *right* now.
2. Although practicality beats purity.
3. Although that way may not be obvious at first unless you're Dutch.
4. Beautiful is better than ugly.
5. Complex is better than complicated.
6. Errors should never pass silently.
7. Explicit is better than implicit.
8. Flat is better than nested.
9. If the implementation is easy to explain, it may be a good idea.
10. If the implementation is hard to explain, it's a bad idea.
11. In the face of ambiguity, refuse the temptation to guess.
12. Namespaces are one honking great idea -- let's do more of those!
13. Now is better than never.
14. Readability counts.
15. Simple is better than complex.
16. Sparse is better than dense.
17. Special cases aren't special enough to break the rules.
18. The Zen of Python, by Tim Peters
19. There should be one-- and preferably only one --obvious way to do it.
20. Unless explicitly silenced.
==================================================
```
