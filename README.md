# Period Ranges

![pypi](https://img.shields.io/pypi/v/period_ranges.svg
        "https://pypi.python.org/pypi/period_ranges")

![travis-ci](https://img.shields.io/travis/iivvoo/period_ranges.svg
        "https://travis-ci.org/iivvoo/period_ranges")



Create ranges of spefic interval periods (quarters, weeks, months) each starting at their base date

# Examples

```python
>>> from period_ranges import generate_range, Period

>>> range = list(generate_range(datetime(2016, 2, 12), datetime(2017,4,1), Period.QUARTER))
>>> print(range)
[Quarter 1 of year 2016, Quarter 2 of year 2016, Quarter 3 of year 2016, Quarter 4 of year 2016, Quarter 1 of year 2017, Quarter 2 of year 2017]

>>> print(range[1].start, range[1].end)
2016-04-01 00:00:00 2016-06-30 23:59:59

```


```python
>>> range = list(generate_range(datetime(2016, 2, 12)))
>>> print(range[0], range[0].start, range[0].end)
Month 2 of year 2016 2016-02-01 00:00:00 2016-02-29 23:59:59

```
