from geom_formulae import *
from nose.tools import *

def test_rectangle_area_int():
    assert rectangle_area(1,1) == 1
    assert rectangle_area(4,4) == 16


eps = 1e-6

def test_rectangle_area_double():
    assert 25/4 - eps <rectangle_area(.5) < 25/4 + eps

@raises(TypeError)
def test_rectangle_area_other():
    rectangle_area("string,string")
###########################3


def test_trapezium_area_int():
    assert trapezium_area(1,4,5) == 25/2
    assert trapezium_area(4,7,8) == 33


eps = 1e-6

def test_trapezium_area_double():
    assert 33- eps <rectangle_area(.5) < 33 + eps

@raises(TypeError)
def test_trapezium_area_other():
    trapezium_area("string,string")
    ###