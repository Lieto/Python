'''
Created on 6 Feb 2016

@author: vesakuoppala
'''
from Graph import Graph

g = { "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : []
    }


graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print("Add vertex:")
graph.add_vertex("z")

print("Vertices of graph:")
print(graph.vertices())
 
print("Add an edge:")
graph.add_edge({"a","z"})
    
print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print('Adding an edge {"x","y"} with new vertices:')
graph.add_edge({"x","y"})
print("Vertices of graph:")
print(graph.vertices())
print("Edges of graph:")
print(graph.edges())

g2 = { "a" : ["d","f"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}

complete_graph = { 
    "a" : ["b","c"],
    "b" : ["a","c"],
    "c" : ["a","b"]
}

isolated_graph = { 
    "a" : [],
    "b" : [],
    "c" : []
}


graph = Graph(g2)
print(graph.density())

graph = Graph(complete_graph)
print(graph.density())

graph = Graph(isolated_graph)
print(graph.density())

g3 = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
}

g4 = { "a" : ["d","f"],
       "b" : ["c"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}

g5 = { "a" : ["d","f"],
       "b" : ["c","b"],
       "c" : ["b", "c", "d", "e"],
       "d" : ["a", "c"],
       "e" : ["c"],
       "f" : ["a"]
}


graph = Graph(g3)
print(graph)
print(graph.is_connected())

graph = Graph(g4)
print(graph)
print(graph.is_connected())

graph = Graph(g5)
print(graph)
print(graph.is_connected())

g6 = { "a" : ["c"],
      "b" : ["c","e","f"],
      "c" : ["a","b","d","e"],
      "d" : ["c"],
      "e" : ["b","c","f"],
      "f" : ["b","e"]
}


graph = Graph(g6)

print(graph.find_all_paths("a", "b"))

diameter = graph.diameter()

print(diameter)

