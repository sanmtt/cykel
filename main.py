# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from copy import copy
import random


def distribute(p_dict, num_groups):
    for _ in range(100):
        round = [[] for _ in range(num_groups)]
        failed = False
        i = 0
        people_list = [key for key in p_dict.keys()]
        random.shuffle(people_list)
        for p in people_list:
            exc = p_dict[p]
            added = False
            start_i = i
            while not added and not failed:
                i = (i + 1) % num_groups
                if not any([x in round[i] for x in exc]) and not added:
                    round[i].append(p)
                    added = True
                elif i == start_i:
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
            ppg = int(len(people) / num_groups)
            unassigned = copy(p_dict)
            round = []
            round =distribute(p_dict, num_groups)

            if not round:
                failed = True
                break

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

    print(make_groups([i for i in range(12)], [4, 4, 3]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
