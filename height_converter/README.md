# 📏 height converter

This script converts heights from cm to feet and inches. By default, the inches
aren't rounded, but you can specify how many decimal places to round them to. If
the rounding option is chosen but no number of decimal places is specified, the
results will be rounded to the nearest inch.

## 🧑‍💻 usage

```
usage: height_converter.py [-h] [-r [X]] CM_HEIGHTS [CM_HEIGHTS ...]

Convert heights from cm to feet and inches.

positional arguments:
  CM_HEIGHTS           heights in cm (e.g. 182, 160, 180.5, 172.75)

options:
  -h, --help           show this help message and exit
  -r [X], --round [X]  round the result to X decimal places (default: 0)
```

Getting approximate measurements:

```shell
$ python height_converter.py 183 176.5 160
183cm is approximately 6'0.047244094488192445"
176.5cm is approximately 5'9.488188976377955"
160cm is approximately 5'2.9921259842519703"
```

Rounding to the nearest inch (`-r 0` is redundant and gives the same result):

```shell
$ python height_converter.py 182 185 180 -r
182cm is roughly 6'0"
185cm is roughly 6'1"
180cm is roughly 5'11"
```

Rounding to three decimal places:

```shell
$ python height_converter.py 182 185 180 -r 3
182cm is roughly 5'11.654"
185cm is roughly 6'0.835"
180cm is roughly 5'10.866"
```
