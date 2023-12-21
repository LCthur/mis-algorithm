"""This module is about grid/network"""

import logging
import random
import random

from .node import Node
from .vis import network_visualization

# configure the "root logger", from which all logger instances inherit
# this is OPTIONAL, you can also use the default options
logging.basicConfig(
    format='[%(asctime)s: %(levelname)s] %(message)s',
    level=logging.INFO,
)

# set up a logger instance for the current module
LOG = logging.getLogger(__name__)

class Grid:
    """Class grid

        This class is intendend to create the network from a given input.

    """

    def __init__(self, grid_coord = [0,0], grid_type = 'grid', grid_size = 0, neighbors_number = 0):
        self.width = grid_coord[0]
        self.length = grid_coord[1]
        self.grid_type = grid_type
        self.grid_size = grid_size
        self.neighbors_number = neighbors_number
        # dictionary contaning the coordinates in the grid of every node and its id
        self.grid = self.grid_init()
        network_visualization(self.grid, "Initial grid")

    def grid_init(self) -> dict:
        """Initialize grid from given width and length

        Function that initliazes the grid from width and length for a Network instance. 

        Args:
            width: integer describing the width of the grid
            length: integer describing the length of the grid

        Returns:
            A nested dictionary containing the id of each node then a dictionary 
            containing the coordinates x and y and a list of neighbours ids.. 

        Raises:
            TypeError: Description of situation when exception is raised.
        """

        grid = {}
        LOG.info("Grid intialization starting")

        # assigning an index and an id to every node in the network
        if self.grid_type == 'grid':
             grid = self.grid_neighbors(grid, self.width, self.length)
             return grid
        
        else:
             grid = self.random_neighbors(grid, self.grid_size, self.neighbors_number)
             LOG.info(grid)
             return grid

    def random_neighbors(self, grid, grid_size: int, neighbors_number: int):
        node_id = 0
        for i in range(0, grid_size):
            # creating a list of potential neighbors without the actual node
            potential_neighbors = [num for num in range(0, grid_size - 1) if num != i]
            neighbors = []
            j = 0

            while j < neighbors_number:
                # choosing a ranodm number in the list
                random_neighbor = random.choice(potential_neighbors)
                #adding this neighbor to the list of node neighbors
                neighbors.append(random_neighbor)
                # removing this neighbor from the list
                potential_neighbors.remove(random_neighbor)
                j += 1
            grid[node_id] = Node(node_id, neighbors)
            node_id += 1

        LOG.info("Grid is initiailized")
        return grid
            
    def grid_neighbors(self, grid, width: int, length: int):
        node_id = 0
        for row in range(0, length):
            for col in range(0,width):
                neighbours = []

                if row != length - 1 : #has upper neighbour
                    neighbours.append(self.find_id_from_coordinates(col, row + 1, width))
                if col != width - 1: # has right neigbour
                    neighbours.append(self.find_id_from_coordinates(col + 1, row, width))
                if row != 0: #has a down neighbour
                    neighbours.append(self.find_id_from_coordinates(col, row - 1, width))
                if col != 0: #has left neihbour
                    neighbours.append(self.find_id_from_coordinates(col - 1, row , width))

                grid[node_id] =  Node(node_id, neighbours)
                node_id += 1
                #returning grid
        LOG.info("Grid is initiailized")
        return grid

    def find_id_from_coordinates(self, x: int, y: int, width: int) -> int:
        """calculate id of the node based on coordinate"""

        calculated_id = y * width + x
        return calculated_id

    def first_exchange(self, probability: float, node: Node):
        """Perform first exchange"""

        node.v = 0 #reset the state before first exchange

        rand_number = random.random() # generates a number between 0 and 1
        if rand_number <= probability: # broadcast if probability is reached
            print("---------------------------------")
            print("ID ", node.node_id, ": is broadcasting")
            node.v = 1

            # broadcast the message to the neigbours by turning their v to 0
            for i in node.neighbors:
                neighbor = self.grid[i]
                neighbor.receive_message()
             # wait half a second that all parallel nodes are reaching the same point

    def second_exchange(self, node: Node) -> str:
        """Perform second exchange"""

        # check if neighbor has broadcasted and if node is active
        if node.active and node.v == 1:

            # deactivate the neighbors, similar to broadcasting
            for i in node.neighbors:
                neighbor = self.grid[i]
                neighbor.deactivate(node.node_id)

            # join MIS and node is therefore deactivated  
            node.join_mis()
            # visualize when a node joins MIS
            network_visualization(self.grid, "Node " + str(node.node_id) + " joined MIS")
            return 'stop' # indicate to MIS class to exit the algorithm

        else: # in this case, v = 0, so neighbor has broadcasted or didn't reach the probability
            for i in node.neighbors:
                neighbor = self.grid[i]
                if neighbor.mis:
                    node.deactivate(neighbor.node_id)
                    return 'stop'

