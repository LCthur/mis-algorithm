"""This module performs MIS algorithm"""

import math
from .grid import Grid
from .node import Node

class MIS:
    """Class for running core algorithm

        Initialize class by network/grid information

        Args:
            active_nodes: IDs of nodes
            MIS_nodes: IDs of MIS nodes
    """

    def __init__(self, grid: Grid):
        self.grid = grid
        self.upper_bound = len(self.grid.grid)
        self.m_value = 34 #random at the moment should be defined by the paper but couldn't find it.

    def get_probability(self, iteration: int) -> float:
        """Calculate broadcast probability

        Calculate the probability with given iteration which is needed during broadcasting.

        Args:
           iteration: current iteration

        Returns:
            probability for broadcast
        """
        return (1 / pow(2, (math.log(self.upper_bound) - iteration)))

    def run_algorithm_on_node(self, nodes: list[Node]):
        """Run MIS algorithm

        Perform first and sencond exchange of MIS algorithm.

        Args:
           node: a Node object to run the algorithm on

        Returns:
            no return
        """
        for i in range(0, math.ceil(math.log(self.upper_bound))):
            for j in range(0, round(self.m_value * math.log(self.upper_bound))):
                for node in nodes:
                    if node.active: # check that the node is still active
                        self.grid.first_exchange(self.get_probability(i), node)
                        self.grid.second_exchange(node)
                    else:
                        j += 1
