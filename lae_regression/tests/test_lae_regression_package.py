"""Test the lae_regression package."""

import unittest
from lae_regression import l1_fit
import numpy as np

def test_version_is_string():
    import lae_regression
    assert isinstance(lae_regression.__version__, str)

class TestL1FitTrivial0(unittest.TestCase):

    def get_U(self):
        "trivial example U"
        return ([1], [2])

    def get_v(self):
        return (0, 1)

    def do_regression(self):
        U = self.get_U()
        v = self.get_v()
        return l1_fit(U, v)

    expected_m = [1]
    expected_k = [-1]

    def test_valid_result(self):
        result = self.do_regression()
        m = result["m"]
        k = result["k"]
        self.assertTrue(np.allclose(m, self.expected_m), repr((m, self.expected_m)))
        self.assertTrue(np.allclose(k, self.expected_k), repr((k, self.expected_k)))

class TestL1fit1DNontrivial(TestL1FitTrivial0):

    def get_U(self):
        return ([1], [2], [3])

    def get_v(self):
        return (0, 0, 1)
    
    expected_m = [ 0.5]
    expected_k = -0.5

class TestL1fit1DOutlier(TestL1FitTrivial0):

    def get_U(self):
        n = 10
        x = np.linspace(0,1,n)
        y = 0.5 * x - 1
        y[5] = 5
        self.y = y
        U = x.reshape((n, 1))
        return U

    def get_v(self):
        return self.y  # assuming get_U is called first :)
    
    expected_m = [ 0.5]
    expected_k = -1
