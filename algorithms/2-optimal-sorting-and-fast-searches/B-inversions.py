def merge_sort(arr, n):

    temp = [0]*n

    return merge_sort_util(arr, temp, 0, n - 1)


def merge_sort_util(arr, temp, left, right):
    count = 0

    if left < right:
        mid = (left + right) // 2
        count += merge_sort_util(arr, temp, left, mid)
        count += merge_sort_util(arr, temp, mid + 1, right)
        count += merge(arr, temp, left, mid, right)

    return count


def merge(arr, temp, left, mid, right):

    i = left
    k = left
    j = mid + 1

    count = 0

    while i <= mid and j <= right:

        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for val in range(left, right + 1):
        arr[val] = temp[val]

    return count


with open('inverse.in', 'r') as f:
    n = int(f.readline())
    s = list(map(int, f.readline().split()))

count = merge_sort(s, n)

with open('inverse.out', 'w') as f:
    print(count, file=f)
