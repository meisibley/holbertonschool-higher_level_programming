#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        list_result = [None] * len(my_list)
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                list_result[i] = True
            else:
                list_result[i] = False
        return list_result
    else:
        return None
