# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from copy import copy
import random


def distribute(p_dict, num_groups):
    """
    Fördela alla i grupper

    TODO: Fixa så att man har en person från förra gruppen som kommer till nästa. Kolla om det är svårt att bestämma host.

    :param p_dict: Personer och vilka de har träffat
    :param num_groups: Antal grupper
    :return:
    """
    for _ in range(100):
        round = [[] for _ in range(num_groups)]
        failed = False
        i = 0
        people_list = [key for key in p_dict.keys()]
        random.shuffle(people_list)
        for p in people_list:
            exc = p_dict[p]  # Personer som inte kan ingå i samma grupp
            added = False
            start_i = i
            while not added and not failed:
                i = (i + 1) % num_groups
                if not any([x in round[i] for x in exc]) and not added:
                    round[i].append(p)
                    added = True
                elif i == start_i:  # Fail efter att ha testat alla grupper
                    failed = True
        if not failed:
            return round
    return None

def make_groups(people: list, number_of_groups: list):
    while True:
        failed = False
        group_list = []
        p_dict = {}
        for p in people:
            p_dict.update({p: []})
        for num_groups in number_of_groups:
            round = distribute(p_dict, num_groups)  # Gör en runda

            if not round:
                failed = True
                break

            # Lägg till personer som inte kan ingå i samma runda
            for g in round:
                for p1 in g:
                    for p2 in g:
                        if p1 != p2:
                            p_dict[p1].append(p2)

            group_list.append(round)
            print(round)
            print(p_dict)
        if failed == False:
            return group_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    failed = True
    while failed:
        failed = False
        round_list = make_groups([i for i in range(12)], [3, 3, 3, 3])
        for round in round_list:
            # Uteslut lista om den innehåller för små grupper.
            for group in round:
                if len(group) < 3:
                    failed = True
    print(round_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
