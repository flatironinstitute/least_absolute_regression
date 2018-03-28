"""
Least absolute error linear regression.
"""

import numpy as np
import scipy.optimize

def l1_fit(U, v):
    """
    Find a least absolute error solution (m, k) to U * m + k = v + e.
    Minimize sum of absolute values of vector e (the residuals).

    Returned result is a dictionary with fit parameters result["m"] and result["k"]
    and other information.
    """
    U = np.array(U)
    v = np.array(v)
    # n is the number of samples
    n = len(v)
    s = U.shape
    assert len(s) == 2
    assert s[0] == n
    # d is the number of dimensions
    d = s[1]
    I = np.identity(n)
    n1 = np.ones((n,1))
    A = np.vstack([
            np.hstack([-I, U, n1]),
            np.hstack([-I, -U, -n1])
        ])
    c = np.hstack([np.ones(n), np.zeros(d+1)])
    b = np.hstack([v, -v])
    bounds = [(0, None)] * n + [(None, None)] * (d+1)
    options = {"maxiter": 10000}
    # Call the linprog subroutine.
    r = scipy.optimize.linprog(c, A, b, bounds=bounds, options=options)
    # Extract the interpolation result from the linear program solution.
    x = r.x
    m = x[n:n+d]
    k = x[n+d]
    v_predicted = np.dot(U, m) + k
    residuals = v - v_predicted
    # For debugging store all parameters, intermediates and results in returned dict.
    result = {}
    result["U"] = U
    result["v"] = v
    result["m"] = m
    result["k"] = k
    result["r"] = r
    result["samples"] = n
    result["dimensions"] = d
    result["A"] = A
    result["b"] = b
    result["c"] = c
    result["bounds"] = bounds
    result["residuals"] = residuals
    result["v_predicted"] = v_predicted
    return result
