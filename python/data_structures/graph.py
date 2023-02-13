class Vertex:
    def __init__(self, node, weight=0):
        self.vertex = node
        self.value = node
        self.weight = weight

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, node, weight=0):
        self.edges.append(Vertex(node, weight))

    def __repr__(self):
        return str(self.value)


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        node = Node(value)
        self.nodes[node.value] = node
        return node

    def add_edge(self, node1, node2, weight=0):
        if node1.value not in self.nodes:
            raise KeyError(f"{node1.value} is not in the graph")
        if node2.value not in self.nodes:
            raise KeyError(f"{node2.value} is not in the graph")
        if node1 == node2:
            self.nodes[node1.value].add_edge(node1, weight)
        else:
            self.nodes[node1.value].add_edge(node2, weight)
            self.nodes[node2.value].add_edge(node1, weight)

    def get_nodes(self):
        return list(self.nodes.keys())

    def get_neighbors(self, node):
        return self.nodes[node.value].edges

    def size(self):
        return len(self.nodes)


class KeyError(Exception):
    pass
