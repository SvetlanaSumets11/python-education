"""This module to implement the graph"""

from linked_list import LinkedList

class LinkedListGraph(LinkedList):
    """A linked list class for a graph"""
    def __init__(self):
        super().__init__()


    def delete_edge_vertex(self, value):
        """Method of removing all edges that contain
        a vertex with a specified value"""
        if self.is_empty():
            print("Список пуст")
        else:
            current = self.head
            ind = 0

            while current is not None:
                if value in current.value:
                    self.delete(ind)
                else:
                    ind += 1
                current = current.next

class Graph:
    """Graph class"""
    def __init__(self):
        self.vertex = LinkedListGraph()
        self.edges = LinkedListGraph()

    def edge_exists(self, vertex_1, vertex_2):
        """Method for checking the existence of an edge"""
        return self.edges.is_value((vertex_1, vertex_2))

    def vertex_exists(self, value):
        """Vertex Existence Testing Method"""
        return self.vertex.is_value(value)

    def add_edge(self, vertex_1, vertex_2):
        """Edge adding method"""
        if self.edges.is_empty() or not self.edge_exists(vertex_1, vertex_2):
            self.edges.append((vertex_1, vertex_2))
        else:
            raise ValueError("Такое ребро уже существует")

    def add_vertex(self, value):
        """Vertex addition method"""
        if self.vertex.is_empty() or not self.vertex_exists(value):
            self.vertex.append(value)
        else:
            raise ValueError("Такая вершина уже существует")

    def delete_edge(self, vertex_1, vertex_2):
        """Rib removal method"""
        if self.edge_exists(vertex_1, vertex_2):
            self.edges.delete_value((vertex_1, vertex_2))
        else:
            raise ValueError("Такого ребра не существует")

    def delete_vertex(self, value):
        """Vertex removal method"""
        if self.vertex_exists(value):
            self.edges.delete_edge_vertex(value)
            self.vertex.delete_value(value)
        else:
            raise ValueError("Такой вершины не существует")

    def __str__(self):
        current_vertex = self.vertex.head
        string = ''
        while current_vertex is not None:
            string += str(current_vertex.value)
            string +=' -> '
            current_vertex = current_vertex.next
        string += 'None\n'

        current_edge = self.edges.head
        while current_edge is not None:
            string += str(current_edge.value)
            string +=' -> '
            current_edge = current_edge.next
        string += 'None'
        return string


# graph = Graph()
# graph.add_vertex(1)
# graph.add_vertex(2)
# graph.add_vertex(3)
# graph.add_vertex(4)
# graph.add_vertex(5)
# graph.add_edge(1, 2)
# graph.add_edge(2, 1)
# graph.add_edge(2, 3)
# graph.add_edge(3, 1)
# graph.add_edge(4, 1)
# graph.add_edge(4, 5)
# graph.add_edge(5, 2)

# print(graph)
# graph.delete_vertex(2)
# print(graph)
# graph.delete_edge(4, 5)
# print(graph)
