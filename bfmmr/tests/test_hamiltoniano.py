from bfmmr import is_hamiltonians_cycle
import networkx as nx
def test_is_hamiltonians_cycle():
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0)])
    cycle = [0, 1, 2]
    assert is_hamiltonians_cycle(G, cycle) == True

    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2)])
    cycle = [0, 1, 2]
    assert is_hamiltonians_cycle(G, cycle) == False

    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])
    cycle = [0, 1, 2]
    assert is_hamiltonians_cycle(G, cycle) == False