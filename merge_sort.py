from RecursiveCounter import *


def merge_sort(invoker, l, start, end):
    if end - start < 2:
        return
    mid = int((start + end) / 2)

    invoker.invoke(l, start, mid)
    invoker.invoke(l, mid, end)

    left = start
    right = mid
    q = []

    while left < mid and right < end:
        if l[left] < l[right]:
            q.append(l[left])
            left += 1
        else:
            q.append(l[right])
            right += 1

    while left < mid:
        q.append(l[left])
        left += 1

    while right < end:
        q.append(l[right])
        right += 1

    for idx in range(start, end):
        l[idx] = q[idx - start]


def is_sorted(l):
    if len(l) < 2:
        return True

    previous = l[0]

    for item in l:
        if previous > item:
            return False
        previous = item

    return True


l = [8, 4, 5, 3, 7, 6, 1, 2]
counter = RecursiveCounter.create_recursive_counter(merge_sort)
counter.invoke(l, 0, len(l))
print("list : {}, is sorted? {}, count : {}".format(l, is_sorted(l), counter.get_count()))
