import copy

class State:
    def __init__(self, arr: list[int], level: int):
        self.level = level # item's serial number
        self.arr = []
        for item in arr: 
            self.arr.append(item) # initial

    def inc_level(self):
        self.level += 1 # next item
    
    def update_state(self, pos: int, val: int):
        self.arr[pos] += val # new valuation

    def __eq__(self, other):
        if self.arr == other.arr and self.level == other.level:
            return True
        return False
    
    def get_min_val(self): # get min valuation of a player in a state
        return min(self.arr)

    def __str__(self):
        return f'{self.arr}'

    def __repr__(self):
        return self.__str__()
###
# generate all states, I did sort of BFS to create each state.
# ###
def states_genarator(items: list[list[int]], player_amount: int):
    root = State([0]*player_amount, 0) # start state, all zeros
    all_states_list = []
    queue = []
    queue.append(root)

    while(items): # while there is items
        new_queue = []
        item = items.pop(0)
        for state in queue: # for each state, we add the preferences of each player to a new state.
            for i in range(player_amount):
                new_state = copy.deepcopy(state)
                new_state.update_state(i, item[i])
                new_state.inc_level()
                new_queue.append(new_state)
        all_states_list += queue
        queue = copy.deepcopy(new_queue)
    all_states_list += queue
    return all_states_list, queue

###
# generate all states, I did sort of BFS to create each state.
# ###
def states_genarator_pruning(items: list[list[int]], player_amount: int):
    root = State([0]*player_amount, 0) # start state, all zeros
    all_states_list = []
    queue = []
    queue.append(root)

    while(items): # while there is items
        new_queue = []
        item = items.pop(0)
        for state in queue: # for each state, we add the preferences of each player to a new state.
            for i in range(player_amount):
                new_state = copy.deepcopy(state)
                new_state.update_state(i, item[i])
                new_state.inc_level()
                if new_state not in new_queue: # if the state is in the list we don't append it.
                    new_queue.append(new_state)
        all_states_list += queue
        queue = copy.deepcopy(new_queue)
    all_states_list += queue
    return all_states_list, queue
"""
get the best state, the one with the max value of the fewer player's preference.
"""
def best_state(final_states: list[State]):
    min_val = -1
    res = None
    for state in final_states:
        state_min_val = state.get_min_val()
        if state_min_val > min_val:
            min_val = state_min_val
            res = state
    return res

"""
Q1 Tests
"""
items0 = [[1,1], [2,2], [3,3], [4,4]]
all_states0, final_states0 = states_genarator(items=copy.deepcopy(items0), player_amount=2)
print(f'all states:\n{all_states0}\n')
print(f'final states:\n{final_states0}\n')
print(f'best state:\n{best_state(final_states0)}\n')


"""
Q2 Tests
"""
items = [[11,22,33], [11,22,44]]
all_states, final_states = states_genarator(items=copy.deepcopy(items), player_amount=3)
all_states_pruning, final_states_pruning = states_genarator_pruning(items=copy.deepcopy(items), player_amount=3)
print(f'all states with out pruning:\n{all_states}\n')
print(f'all states with pruning:\n{all_states_pruning}\n')
print(f'number of states with pruning = {len(all_states_pruning)}\nnmber of states with out pruning = {len(all_states)}')

