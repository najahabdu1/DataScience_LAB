def common_ele(list1, list2):
    res = False

    # traverse in the 1st list
    for x in list1:

        # traverse in the 2nd list
        for y in list2:

            # if one common
            if x == y:
                res = True
                return res

    return res


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 5]
print(common_ele(a, b))
