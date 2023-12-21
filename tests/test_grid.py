import pytest
from src.grid import Grid
from src.node import Node





# create an instance of Grid to make test on
width = 3
length = 3

g = Grid([width, length])
node = Node(4, [1,5,7,3])



def test_add():
    # testing grid edges for a 3x3 matrix
    assert g.find_id_from_coordinates(0, 0, 3) == 0
    assert g.find_id_from_coordinates(2, 2, 3) == 8
    assert g.find_id_from_coordinates(0, 2, 3) == 6
    assert g.find_id_from_coordinates(0, 0, 3) == 0

    # checking that grid is a dictionary
    assert isinstance(g.grid, dict)

    # Checking that grid is populated by instances of Node
    assert isinstance(g.grid[1], Node)
    
    # make sure that if input is not converted to int, a TypeError is raised by python
    with pytest.raises(TypeError):
        g.grid_init('5', 1)
    
    with pytest.raises(TypeError):
        g.grid_init(5, '3')

    with pytest.raises(TypeError):
        g.grid_init('5', '3')

    # checking that with a probability of 100% the state.v of the node changes to 1
    assert node.v == 0
    g.first_exchange(1, node)
    assert node.v == 1

    # checking that if probability is not reached there is no change of v state
    g.first_exchange(0, node)
    assert node.v == 0

    # checking that the node broadcast and join MIS in the second exchange if v == 1 and node.active
    if node.v == 1 and node.active:
        g.second_exchange(node)
        assert node.mis is True

    # checking that there is no broadcast if a message is received by one of the neighbors
    node.v = 0
    g.second_exchange(node)
    assert node.mis is False

    


    