import random

class Vertex(object):
    def __init__(self,value):
        self.value = value
        self.adjacent = {} #keeps track of which vertices (keys) are attached, and their weights (values)
        self.neighbours = []
        self.neighbours_weights = []

    def __str__(self):
        return self.value + " ".join([node.value for node in self.adjacent.keys()])

    def add_edge_to(self,vertex,weight=0):
        #adding an edge, and its associated weight, to a vertex
        self.adjacent[vertex] = weight

    def increment_edge(self,vertex):
        # incrementing weight of the edge when it already exists
        self.adjacent[vertex] = self.adjacent.get(vertex,0) + 1

    def get_probability_map(self): #map each word to its probability but put them in separate lists
        for (vertex, weight) in self.adjacent.items():
            self.neighbours.append(vertex)
            self.neighbours_weights.append(weight)

    def next_word(self):
        return random.choices(self.neighbours, weights = self.neighbours_weights)[0] #index 0 to get top word


class Graph:
    def __init__(self):
        # string to vertex mapping
        # whenever we encounter a new word, can look it up in this dict to get the vertex object
        self.vertices = {}

    def get_vertex_values(self):
        # return values of all vertices
        return set(self.vertices.keys())

    def add_vertex(self, value): # value is the word the vertex represents
        self.vertices[value] = Vertex(value) # here we created a new vertex object from class Vertex

    def get_vertex(self, value): # will give us the vertex object that a given word represents
        if value not in self.vertices:
            self.add_vertex(value) #create new vertex if the word doesnt exist yet
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()

