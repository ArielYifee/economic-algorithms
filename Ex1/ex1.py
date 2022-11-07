import doctest

class Agent:

    def __init__(self, values: list):
        self.values = values

    def value(self, option: int) -> float:
        return self.values[option]

x = Agent([1,2,3,4,5])
y = Agent([3,1,2,5,4])
z = Agent([3,5,5,1,1])

AgentList = [x,y,z]

def isParetoImprovement(agents: list, option1: int, option2: int) -> bool:
    """
    >>> isParetoImprovement(AgentList, 2,1)
    True
    >>> isParetoImprovement(AgentList, 1,2)
    False
    """
    for agent in agents:
        # print(f"{agent.value(option1)}, {agent.value(option2)}")
        if agent.value(option1) < agent.value(option2):
            return False
    return True


def isParetoOptimal(agents: list, option: int, allOptions: list):
    """
    >>> isParetoOptimal(AgentList, 0, [1,2,3,4])
    True
    >>> isParetoOptimal(AgentList, 1, [0,2,3,4])
    False
    """
    for opt in allOptions:
        if isParetoImprovement(agents, opt, option) and opt != option:
            return False
    return True

doctest.testmod()