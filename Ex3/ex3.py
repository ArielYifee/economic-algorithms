"""
In this exercise, I didn't refer to the surplus vote agreement.
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

election_result = {
    "likud": 1115336,
    "yesh_atid": 847435,
    "zionot_datit": 516470,
    "gantz": 432482,
    "shas": 392964,
    "gimel": 280194,
    "israel_bietenu": 213687,
    "united_arabs": 194047,
    "hadash_taal": 178735,
    "avoda": 175992
}

mandate_result = {
    "likud": 32,
    "yesh_atid": 24,
    "zionot_datit": 14,
    "gantz": 12,
    "shas": 11,
    "gimel": 7,
    "israel_bietenu": 6,
    "united_arabs": 5,
    "hadash_taal": 5,
    "avoda": 4
}

mandate_without_apparentment = {
    "likud": 31,
    "yesh_atid": 24,
    "zionot_datit": 14,
    "gantz": 12,
    "shas": 11,
    "gimel": 7,
    "israel_bietenu": 6,
    "united_arabs": 5,
    "hadash_taal": 5,
    "avoda": 5
}

def mandate_divisioner(election_result: dict, mandate_result: dict, divisor_method, y:float=0.0, log:bool=False):
    mandate_division = {
        "likud": 0,
        "yesh_atid": 0,
        "zionot_datit": 0,
        "gantz": 0,
        "shas": 0,
        "gimel": 0,
        "israel_bietenu": 0,
        "united_arabs": 0,
        "hadash_taal": 0,
        "avoda": 0
    }
    next_mandate = ""
    highest_portion = 0
    left_spots = 120
    while left_spots > 0:
        next_mandate = ""
        highest_portion = 0
        for party in election_result:
            portion = divisor_method(election_result[party], mandate_division[party], y)
            if portion > highest_portion:
                highest_portion = portion
                next_mandate = party
        mandate_division[next_mandate] += 1
        left_spots -= 1
    if log:
        print(f"new mandate division:\n{mandate_division}")
    winners = []
    losers = []
    for mandate in mandate_result:
        winners.append(mandate) if mandate_division[mandate] >= mandate_result[mandate] else losers.append(mandate)
    if log:
        print(f"the winners:\n{winners}")
        print(f"the losers:\n{losers}")
    return mandate_division

def f(election_result:int, current_mandate: int, y:float):
    return election_result / (current_mandate + y)


print(f"{bcolors.HEADER}Section A:{bcolors.ENDC}")
mandate_divisioner(election_result=election_result, mandate_result=mandate_result, divisor_method=f, y=0.5, log=True)

print(f"{bcolors.HEADER}Section B:{bcolors.ENDC}")

y = 1.0 # I am starting with 1 because in Israel we use the Jefferson method.
while True:
    if mandate_divisioner(election_result=election_result, mandate_result=mandate_result, divisor_method=f, y=y, log=False) != mandate_without_apparentment:
        print(f"The largest y that give diffrent division is: {y}")
        break
    y += 0.001
