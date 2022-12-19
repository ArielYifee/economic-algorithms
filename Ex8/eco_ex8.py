import numpy as np
import math
import itertools

#function that sumarize a matrix
def build_sum_array(build: np.ndarray, arr: np.ndarray, player: int, player_num: int, option: list[float], option_num: int, flag: bool):
    sum = 0.0
    for i in range(0, player_num):
        if i != player or flag: # flag that mark if ignore a player or not
            sum += arr[i][option[i]]
    build[player][option_num] = sum
    return build


def VCG(arr: list[list[float]]):
    if len(arr) != len(arr[0]):
        raise Exception("not Square matrices")  # checking input

    player_num = len(arr)  # number of player
    option_num = math.factorial(player_num)  # number of possible options
    sum_of_option = np.zeros(shape=(1, option_num)) # array that will contain the sum of each option
    OWP = np.zeros(shape=(player_num, option_num))  # array of each option without a player
    np_arr = np.array(arr) # converting the array to numpy array
    options = list(itertools.permutations(range(0, player_num))) # array of all option (every combinations)
    print(options)
    for i in range(0, option_num): # for each option sum the value of each player
        sum_of_option = build_sum_array(build=sum_of_option, arr=np_arr, player=0,
                                  player_num=player_num, option=options[i], option_num=i, flag=True)

    for i in range(0, player_num): # build the sum of each option without a player
        for j in range(0, option_num):
            OWP = build_sum_array(build=OWP, arr=np_arr, player=i, player_num=player_num,
                            option=options[j], option_num=j, flag=False)
    float_formatter = "{:.1f}".format
    np.set_printoptions(formatter={'float_kind':float_formatter})
    print(f'sum of all option:')
    print(np.array2string(sum_of_option, separator=", "))
    print()

    index = sum_of_option.argmax() # the option with max sum
    print(f'the max option is option number {index+1}')
    print()

    print(f'sum of each option without a player:')
    print(np.array2string(OWP, separator=", "))

    print()

    payment = np.zeros(shape=(player_num, 3)) # array that calculates the payment and profit of each player
    for i in range(0, player_num):
        max = np.max(OWP[i])
        if OWP[i].argmax() != index: # if the player was influent on the result he will pay the remainder
            payment[i][0] = (max - OWP[i][index])
        else:
            payment[i][0] = 0 # if the player wasn't influent on the result he will not pay
        payment[i][1] = np_arr[i][options[index][i]]
        payment[i][2] = payment[i][1] - payment[i][0]

    print(f'summary:')
    print(np.array2string(payment, separator=", "))

a = [[4, 10], [5, 9]]
b = [[8, 4, 3], [5, 8, 1], [3, 5, 3]]
VCG(b)
