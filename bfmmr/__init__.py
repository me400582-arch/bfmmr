import itertools   # para hacer las permutuaciones
import networkx as nx 
from itertools import product

""" Checks if cycle is a Hamiltonian cycle in graph.graph is a Networkx graph, and cycle is a list of vertices"""
def is_hamiltonians_cycle(graph, cycle):              #Se define la funcion
    n = len (set(cycle))                  # se usa SET para que los n se verla como conjuntos
    if n != graph.order():                    # se hace un conjunto los vertices para que no se repitan
        return False
    for i in range(n-1):                          # se guarda los n vertices con un for, empezando i=o
        if not graph.has_edge(cycle[i], cycle[i+1]):   # se usa por si un arista no es amigo de otro por lo tanto no termina el ciclo al inicio y al final
            return False
        if not graph. has_edge(cycle[n-1], cycle[0]):
            return False
        return True
def is_hamiltonians(graph):      # se usa para conocer las permutaciones
    if not nx.is_connected(graph):
        return False
    vertices = list(graph.nodes())
    if len(vertices) < 3:      # los vertices son menor de 3 entonce no cumple que sea ciclo hamiltoniano, es decir debe de tener 3 para ser un ciclo
        return False
    perms = itertools.permutations(vertices)
    for perm in perms:        # solo las inicia
        if is_hamiltonian_cycle(graph, perm):  # si ya encontro el ciclo hamiltoniano
            return perm
    return False


def is_proper_coloring(graph,coloring):    #determina en si o no
  for edge in graph.edges():      #edges () es una lista de las aristas
    if coloring[edge[0]] == coloring[edge[1]]:   #para hacer una colorcion propia
      return False
  return True

def is_3_coloring(graph):   # si es colorable 3 verdader por lo contrio que no regrese
    n = graph.order()    # preguntar cuantas vertices
    colorings = product([0,1,2], repeat = n)
    for coloring in colorings:
        if is_proper_coloring (graph, coloring):
          return coloring
    return False
