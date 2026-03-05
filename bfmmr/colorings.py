from itertools import product

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
