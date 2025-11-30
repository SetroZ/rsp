class UND_GRAPH:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, u):
        self.graph[u] = []

    def remove_vertex(self, u):
        del self.graph[u]
        for k in self.graph:
            self.graph[k].remove(u)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)
