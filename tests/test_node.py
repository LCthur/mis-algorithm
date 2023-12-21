import pytest
from src.node import Node

node = Node(4, [1,5,7,3])


def test_add(): 
    # testing initial state of Node
    assert node.active is True
    assert node.mis is False
    assert node.v == 0

    # testing if join_mis functions works
    node.join_mis()
    assert node.mis is True
    assert node.active is False

    # testing if receive message works
    node.receive_message()
    assert node.v == 0

    #testing deactivate function
    node.active = True
    node.deactivate()
    assert node.active is False

    assert isinstance(node.neighbors, list)
    