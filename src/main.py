"""This is a main module"""

from .grid import Grid
from .MIS import MIS
from .vis import network_visualization

def main():
    """Main function"""
    while True: 
        grid_type = str(input("Enter the type of network you want: [grid/random]: "))
        print(grid_type)
        if grid_type == "grid" or grid_type == "random": 
            break
        print("Wrong choice, try again !")
    # ask size of the grid from user

    if grid_type == 'grid':
        grid_width = int(input("Enter width of grid: "))
        grid_length = int(input("Enter length of grid: "))

        grid = Grid([grid_width, grid_length]) # initialize grid

    else:
        while True: 
            grid_size = int(input("Enter the number of nodes in your network: "))
            neighbors_n = int(input("Enter the number of neighbors per node: "))
            if grid_size > neighbors_n:
                grid = Grid(grid_type = grid_type, grid_size = grid_size, neighbors_number= neighbors_n)    
                break
            print("You have more neighbors than nodes in the network, it's not serious... Try again")
    
    
    
    mis = MIS(grid) # initialize MIS with grid
    nodes = list(grid.grid.values())

    mis.run_algorithm_on_node(nodes)

    # get MIS nodes and make list of them
    mis_nodes = []
    for node in nodes:
        if node.mis:
            mis_nodes.append(node.node_id)

    # print IDs of MIS nodes on terminal
    print("---------------------------------")
    print("MIS nodes: ", mis_nodes)

    # visualize final netwrok of MIS
    network_visualization(grid.grid, "Final result")

if __name__ == "__main__":
    main()
