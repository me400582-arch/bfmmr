from bfmmr import is_proper_coloring    
import networkx as nx
import itertools    
def test_is_proper_coloring():  
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0)])
    coloring = [0, 1, 2]
    assert is_proper_coloring(G, coloring) == True

    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0)])
    coloring = [0, 0, 0]
    assert is_proper_coloring(G, coloring) == False

    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])
    coloring = [0, 1, 0, 1]
    assert is_proper_coloring(G, coloring) == True

