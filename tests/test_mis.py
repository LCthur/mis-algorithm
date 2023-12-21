import pytest
import math
from src.MIS import MIS
from src.grid import Grid


width = 3
length = 3

g = Grid([width, length])
m = MIS(g)

def test_add():
    # making sure that get_proability doesn't accept string
    with pytest.raises(TypeError):
        m.get_probability('test')

    # checking that upper bound is the length of the grid
    assert m.upper_bound == len(g.grid)
    assert m.m_value == 34

    assert m.get_probability(math.log(m.upper_bound)) <= 1





