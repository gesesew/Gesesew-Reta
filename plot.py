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
