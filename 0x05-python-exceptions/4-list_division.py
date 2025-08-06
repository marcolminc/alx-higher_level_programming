#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for i in range(list_length):
        ratio = 0
        try:
            ratio = my_list_1[i] / my_list_2[i]
        except IndexError:
            print('out of range')
        except ZeroDivisionError:
            print('division by 0')
        except (TypeError, ValueError):
            print('wrong type')
        finally:
            res_list.append(ratio)
    return res_list
