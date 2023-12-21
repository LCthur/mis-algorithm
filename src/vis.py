"""This module is for the visualization"""

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def network_visualization(grid: dict, title: str):
    """Visualization of netowrk

    Function that creates a visualization of the network. 

    Args:
        grid: dictionary containing node_id as keys and Node instances as values

    Returns:
        This function doesn't return anything. It displays the graph in a new window

    Raises:
        TypeError: Description of situation when exception is raised.
    """

    graph = nx.Graph()  # creating empty graph

    # Creating a node for each node in the network and assigning the neighbors
    for node_id in grid:
        # add nodes with color
        if grid[node_id].mis:
            graph.add_node(node_id, nodetype='blue')
        else:
            graph.add_node(node_id, nodetype='green')

        # add edges to the graph
        for neighbor_id in grid[node_id].neighbors:
            # set edge style
            if grid[neighbor_id].deactivated_node == node_id or grid[node_id].deactivated_node == neighbor_id:
                graph.add_edge(node_id, neighbor_id, style='-')
            else:
                graph.add_edge(node_id, neighbor_id, style='--')

    # add node color
    colors = [u[1] for u in graph.nodes(data="nodetype")]

    # add edge style
    styles = [graph[u][v]['style'] for u,v in graph.edges]

    # fix node layout
    pos=nx.kamada_kawai_layout(graph)

    # draw network
    nx.draw(graph, pos=pos, with_labels=True, font_weight='bold', node_color=colors, style=styles)

    # add legend
    legend_elements = [Line2D([0], [0], marker='o', color='w', label='MIS node',
                            markerfacecolor='b', markersize=15),
                        Line2D([0], [0], marker='o', color='w', label='node',
                            markerfacecolor='g', markersize=15)]
    plt.legend(handles=legend_elements)

    # set title
    plt.suptitle(title)
    plt.show()
