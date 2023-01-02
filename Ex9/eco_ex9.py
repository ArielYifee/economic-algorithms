import cvxpy


def Nash_budget(total: float, subjects: list[str], preferences: list[list[str]]):
    allocations = cvxpy.Variable(len(subjects))
     
    utilities = [None]*len(preferences)
    for i, person in enumerate(preferences):
        temp_var = None
        for preference in person:
            if temp_var is None:
                temp_var = allocations[subjects.index(preference)]
            else:
                temp_var += allocations[subjects.index(preference)]
        utilities[i] = temp_var
    
    sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])

    problem = cvxpy.Problem(
    cvxpy.Maximize(sum_of_logs),
    constraints = 
        [v >= 0 for v in allocations] + 
        [cvxpy.sum(allocations)==total]
        )
    problem.solve()

    print("BUDGET:")
    for i, sub in enumerate(subjects):
        print(f'{sub} = {allocations[i].value:.3f}')
    print('\n')
    
    utility_values = [u.value for u in utilities]
    print("UTILS :")
    for val in utility_values:
        print(f'{val:.3f}', end=", ")
    print('\n')

    donations = total/len(preferences)
    for i, person in enumerate(preferences):
        print(f'Citizen {i} should donate: ',end="")
        for preference in person:
            donate = allocations[subjects.index(preference)].value * donations / utilities[i].value
            print(f'{donate:.3f}$ to {preference}',end=", ")
        print()


Nash_budget(total= 500, subjects = ['A', 'B', 'C', 'D'], preferences=[['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['A']])