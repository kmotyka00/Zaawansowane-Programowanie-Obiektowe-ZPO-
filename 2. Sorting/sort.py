# Kacper Motyka, 401666

from typing import List


def quicksort2(copy_of_lst: List[int], start: int, stop: int) -> None:
    i = start
    j = stop
    pivot = copy_of_lst[int(start+(stop-start)/2)]

    while i < j:
        while copy_of_lst[i] < pivot:
            i = i+1
        while copy_of_lst[j] > pivot:
            j = j-1

        if i <= j:
            copy_of_lst[i], copy_of_lst[j] = copy_of_lst[j], copy_of_lst[i]
            i = i+1
            j = j-1
        else:
            break

    if start < j:
        quicksort2(copy_of_lst, start, j)

    if i < stop:
        quicksort2(copy_of_lst, i, stop)


def quicksort(lst: List[int]) -> List[int]:
    copy_of_lst = lst[:]
    start = 0
    stop = len(lst)-1
    quicksort2(copy_of_lst, start, stop)
    return copy_of_lst


def bubblesort2(copy_of_lst: List[int]) -> List[int]:
    num_of_oper = 0
    n = len(copy_of_lst)
    while n>1:
        for i in range(1,n):
            num_of_oper = num_of_oper+1
            if copy_of_lst[i-1] > copy_of_lst[i]:
                copy_of_lst[i-1], copy_of_lst[i] = copy_of_lst[i], copy_of_lst[i-1]
        n = n-1
    return num_of_oper


def bubblesort(lst: List[int]) -> (List[int], int):
    copy_of_lst = lst[:]
    n = bubblesort2(copy_of_lst)
    return copy_of_lst, n




















