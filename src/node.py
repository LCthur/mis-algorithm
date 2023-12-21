"""This module is about individual nodes in grid"""

class Node:
    """Class Node
    
    Args:
        node_id: id of the node
        active: shows if the node is active or not
        neighbors: id's of the node's neighbors
        MIS: indicate if node is MIS or not
        first_message: shows if they received message in first exchange
        deactivated_node: shows which MIS (id) deactivated the node
    """
    def __init__(self, node_id: int, neighbors: list[int]):
        self.node_id = node_id
        self.neighbors = neighbors
        self.mis = False
        self.active = True
        self.v = 0
        self.deactivated_node = -1

    def join_mis(self):
        """Join MIS and deactivate itself if not broadcasted during first exchange"""
        self.mis = True
        print("    * Node", self.node_id, "joined MIS *")
        if self.active:
            self.active = False

    def receive_message(self):
        """set variable v as '0' when receiving message during first exchange"""
        self.v = 0

    def deactivate(self, mis_node_id: int):
        """Deactivate if its neighbor joins MIS"""
        if self.active:
            self.active = False
            self.deactivated_node = mis_node_id
            print("    ID ", self.node_id, ": is deactivated due to node", mis_node_id)
