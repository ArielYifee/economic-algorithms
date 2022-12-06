"""
Q1
helped by:
https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cycles.cycle_basis.html#networkx.algorithms.cycles.cycle_basis
"""
import networkx as nx
import doctest

allocation0 = [
    [0.5,0.5,0],
    [0.5,0.5,0],
    [0,0,1],
]
allocation1 = [
    [0.5,0.5,0],
    [0.5,0,0],
    [0,0,1],
]
def find_cycle_in_consumption_graph(allocation: list[list[float]]):
    """
    >>> find_cycle_in_consumption_graph(allocation=allocation0)
    [[3, 1, 4, 0]]
    >>> find_cycle_in_consumption_graph(allocation=allocation1)
    there is no cycles!
    """
    NXG = nx.Graph()
    players_size = len(allocation)
    elements_size = len(allocation[0])
    
    for player in range(0, players_size):
        for element in range(0, elements_size):
            if allocation[player][element] > 0: # if the element shared with the player
                NXG.add_edge(player, element + players_size) # add the connection of the player with the elemet
    c = list(nx.cycle_basis(NXG))
    if not c:
        print("there is no cycles!")
    else:
        print(c)
        
doctest.testmod()
