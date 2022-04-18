def merge_sort(lst):
    if len(lst) == 1:

        return lst

    else:
        middle = len(lst) // 2
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])

        return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] + right[j] > right[j] + left[i]:
            res.append(left[i])
            i += 1

        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


lst = []

while True:
    try:
        s = input()
    except EOFError:
        break

    lst.append(s)

print(''.join(merge_sort(lst)))
