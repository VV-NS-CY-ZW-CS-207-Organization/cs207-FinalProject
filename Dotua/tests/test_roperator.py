# This file serves to test the operator.py module
from Dotua.roperator import rOperator as op
from Dotua.nodes.rscalar import rScalar
from Dotua.nodes.rvector import rVector
import numpy as np
import math


# initializations
def generate(v=0.75):
    var = rScalar(v)
    var._init_roots()
    return var

# def generatey():
#     return rVector([0.2,0.3])


# Define constants for testing
c1, c2 = 0.5, 1


def test_sin():
    # Test rScalar
    x = generate()
    f = op.sin(x)
    assert f.eval() == np.sin(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == np.cos(x._val)

    # Test constant
    assert op.sin(c1) == np.sin(c1)


    # y = generatey()
    # g = op.sin(y)
    # g._grad_val = 1
    # assert list(y.gradient()) == list(np.cos(y._val))

def test_cos():
    # Test rScalar
    x = generate()
    f = op.cos(x)
    assert f.eval() == np.cos(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == -np.sin(x._val)

    # Test constant
    assert op.cos(c1) == np.cos(c1)

#     y = generatey()
#     g = op.cos(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(-np.sin(y._val))



def test_tan():
    # Test rScalar
    x = generate()
    f = op.tan(x)
    assert f.eval() == np.tan(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == np.arccos(x._val) ** 2

    # Test constant
    assert op.tan(c1) == np.tan(c1)

#     y = generatey()
#     g = op.tan(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(np.arccos(y._val)**2)



def test_arcsin():
    # Test rScalar
    x = generate()
    f = op.arcsin(x)
    assert f.eval() == np.arcsin(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == -np.arcsin(x._val) * np.arctan(x._val)

    # Test constant
    assert op.arcsin(c1) == np.arcsin(c1)

#     y = generatey()
#     g = op.arcsin(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(-np.arcsin(y._val)*np.arctan(y._val))


def test_arccos():
    # Test rScalar
    x = generate(1)
    f = op.arccos(x)
    assert f.eval() == np.arccos(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == np.arccos(x._val) * np.tan(x._val)

    # Test constant
    assert op.arccos(c2) == np.arccos(c2)

    # y = generatey()
    # g = op.arccos(y)
    # g._grad_val = 1
    # assert list(y.gradient()) == list(np.arccos(y._val)*np.tan(y._val))


def test_arctan():
    # Test rScalar
    x = generate()
    f = op.arctan(x)
    assert f.eval() == np.arctan(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == -np.arcsin(x._val) ** 2

    # Test constant
    assert op.arctan(c1) == np.arctan(c1)

#     y = generatey()
#     g = op.arctan(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(-np.arcsin(y._val)**2)


def test_sinh():
    x = generate()
    f = op.sinh(x)
    assert f.eval() == np.sinh(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == np.cosh(x._val)

    # Team constnt
    assert op.sinh(c1) == np.sinh(c1)

#     y = generatey()
#     g = op.sinh(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(np.cosh(y._val))


def test_cosh():
    # Test rScalar
    x = generate()
    f = op.cosh(x)
    assert f.eval() == np.cosh(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == np.sinh(x._val)

    # Test constant
    assert op.cosh(c1) == np.cosh(c1)

#     y = generatey()
#     g = op.cosh(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(np.sinh(y._val))


def test_tanh():
    x = generate()
    f = op.tanh(x)
    assert f.eval() == np.tanh(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == 1 - np.tanh(x._val) ** 2

    # Test constant
    assert op.tanh(c1) == np.tanh(c1)

#     y = generatey()
#     g = op.tanh(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(1-np.tanh(y._val)**2)


def test_arcsinh():
    x = generate()
    f = op.arcsinh(x)
    assert f.eval() == np.arcsinh(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == -np.arcsinh(x._val) * np.arctanh(x._val)

    # Test constant
    assert op.arcsinh(c1) == np.arcsinh(c1)

#     y = generatey()
#     g = op.arcsinh(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(-np.arcsinh(y._val)*np.arctanh(y._val))


def test_arccosh():
    # Test rScalar
    x = generate(1)
    f = op.arccosh(x)
    assert f.eval() == np.arccosh(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == -np.arccosh(x._val) * np.tanh(x._val)

    # Test constant
    assert op.arccosh(c2) == np.arccosh(c2)

#     y = rVector([1,1])
#     g = op.arccosh(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(-np.arccosh(y._val)*np.tanh(y._val))


def test_arctanh():
    # Test rScalar
    x = generate()
    f = op.arctanh(x)
    assert f.eval() == np.arctanh(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == 1 - np.arctanh(x._val) ** 2

    # Test constant
    assert op.arctanh(c1) == np.arctanh(c1)

#     y = generatey()
#     g = op.arctanh(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(1-np.arctanh(y._val)**2)


def test_exp():
    # Test rScalar
    x = generate()
    f = op.exp(x)
    assert f.eval() == np.exp(x._val)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == np.exp(x._val)

    # Test constant
    assert op.exp(c1) == np.exp(c1)

#     y = generatey()
#     g = op.exp(y)
#     g._grad_val = 1
#     assert list(y.gradient()) == list(np.exp(y._val))


def test_log():
    # Test rScalar
    base = 10
    x = generate()
    f = op.log(x, base)
    assert f.eval() == math.log(x._val, base)

    f._grad_val = 1
    f.gradient(x)
    assert x._grad_val == (x._val * math.log(base)) ** (-1)

    # Test constant
    assert op.log(c1, base) == math.log(c1, base)
