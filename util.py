class Node:
    def __init__(self, node_id: str):
        self.id = node_id
        self.adjacent = {}

    def get_id(self):
        return self.id

    def add_neighbor(self, neighbor, weight=1):
        self.adjacent[neighbor] = weight

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def get_neighbors(self):
        return self.adjacent.keys()


class Graph:
    def __init__(self):
        self.nodes = {}
        self.num_vertices = 0

    def get_nodes(self):
        return self.nodes.keys()

    def add_node(self, node_id: str):
        self.num_vertices = self.num_vertices + 1
        node = Node(node_id)
        self.nodes[node_id] = node

        return node

    def add_edge(self, src, dst, cost=1):
        if src not in self.nodes:
            self.add_node(src)
        if dst not in self.nodes:
            self.add_node(dst)

        self.nodes[src].add_neighbor(self.nodes[dst], cost)
        self.nodes[dst].add_neighbor(self.nodes[src], cost)
