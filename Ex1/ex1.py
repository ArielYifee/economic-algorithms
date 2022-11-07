import doctest


class Agent:

    def __init__(self, values: list):
        self.values = values

    def value(self, option: int) -> float:
        return self.values[option]


"""
initialize the agents from the example.
"""
Ami = Agent([1, 2, 3, 4, 5])
Tami = Agent([3, 1, 2, 5, 4])
Rami = Agent([3, 5, 5, 1, 1])

agents = [Ami, Tami, Rami]


def isParetoImprovement(agents: list, option1: int, option2: int) -> bool:
    """
    >>> isParetoImprovement(agents, 2,1)
    True
    >>> isParetoImprovement(agents, 1,2)
    False
    """
    for agent in agents:
        # check if option 1 is better than option 2 for each player.
        if agent.value(option1) < agent.value(option2):
            return False
    return True


def isParetoOptimal(agents: list, option: int, allOptions: list):
    """
    >>> isParetoOptimal(agents, 0, [1,2,3,4])
    True
    >>> isParetoOptimal(agents, 1, [0,2,3,4])
    False
    """
    for opt in allOptions:
        # check for each option if it's better than all the options that are given. 
        if isParetoImprovement(agents, opt, option) and opt != option:
            return False
    return True


doctest.testmod()
