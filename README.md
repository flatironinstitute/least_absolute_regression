[![Build Status](https://travis-ci.org/AaronWatters/least_absolute_regression.svg?branch=master)](https://travis-ci.org/AaronWatters/least_absolute_regression)
[![codecov](https://codecov.io/gh/AaronWatters/least_absolute_regression/branch/master/graph/badge.svg)](https://codecov.io/gh/AaronWatters/least_absolute_regression)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/AaronWatters/least_absolute_regression/master)


# least_absolute_regression

Least absolute error regression implemented using Linear Programming.

Below is an example using 5 samples with 2 independent variables that do not fit a plane.
The mapping of independent variables to the dependent variable is
```
(1,1) --> 0
(1,-1) --> -2
(-1,-1) --> -4
(-1,1) --> -2
(0,0) --> -1.3
```
All but the last mapping fit the plane x + y - 2 = z.

```
from lae_regression import l1_fit
U = ([1, 1], [1, -1], [-1, -1], [-1, 1], [0, 0])
v = (0, -2, -4, -2, -1.3)
result = l1_fit(U, v)
result["m"], result["k"], result["residuals"], result["samples"], result["dimensions"]
```

The value of the last line gives:

```
(array([ 1.,  1.]),
 -2.000,
 array([ -4.441e-16,  -1.332e-15,  -4.441e-16,   4.441e-16,   7.000e-01]),
 5,
 2)
```

Here with `m = (1,1)` and `k = -2` the regression finds the plane
`1*x + 1*y - 2 = z` and essentially rejects the last mapping as an
outlier.

## Background

Historically this code was set up to illustrate techniques for
developing and publishing computational methods using methodologies
associated with Jupyter notebooks.

[Please see the `./presentation` folder for detailed discussion
of the methods used (as jupyter notebooks).](./presentation)

In particular the [`./presentation/Notebooks as Notes.ipynb`](./presentation/1_Notebooks as Notes.ipynb)
notebook introduces concepts of least absolute error regression
and the [`./presentation/1.1_Method%20Derivation.ipynb`](./presentation/1.1_Method Derivation.ipynb)
notebook discussing the derivation of the calculation.
