#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        result = 0
        uniq = 0
        for i in range(len(my_list)):
            result += my_list[i]
            for j in range(i + 1, len(my_list)):
                if my_list[i] == my_list[j]:
                    uniq += my_list[j]
        result -= uniq
        return result
    else:
        return 0
