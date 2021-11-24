#!/usr/bin/python
# -*- coding: utf-8 -*-

from sort import quicksort
from sort import bubblesort
from timeit import timeit
import random

random_list = random.sample(range(1, 1000), 999)
print("random list: ", random_list)

sorted_list = quicksort(random_list)
print("sorted_list: ", sorted_list)

equal_list = []
for i in range(1000):
    equal_list.append(10)
print("equal list: ", equal_list)

# reversed_list = sorted_list
# reversed_list.reverse()
# print("reversed list: ", reversed_list)

reversed_list = []
for i in range(1000, 1, -1):
    reversed_list.append(i)
print("reversed list: ",reversed_list)


#TESTY FUNKCJI BUBBLE
t1_bubble = timeit ( "bubblesort ( random_list ) " , number =1000 , globals = globals ()) #RANDOM
t2_bubble = timeit ( "bubblesort ( sorted_list ) " , number =1000 , globals = globals ()) #SORTED
t3_bubble = timeit ( "bubblesort ( equal_list ) " , number =1000 , globals = globals ()) #EQUAL
t4_bubble = timeit ( "bubblesort ( reversed_list ) " , number =1000 , globals = globals ()) #REVERSED

print("RANDOM TIME FOR BUBBLE: ",t1_bubble)
print("SORTED TIME FOR BUBBLE: ",t2_bubble)
print("EQUAL TIME FOR BUBBLE: ",t3_bubble)
print("REVERSED TIME FOR BUBBLE: ",t4_bubble)

#TESTY FUNKCJI QUICK
t1_quick = timeit("quicksort ( random_list )", number =1000 , globals = globals ()) #RANDOM
t2_quick = timeit ( "quicksort ( sorted_list )" , number =1000 , globals = globals ()) #SORTED
t3_quick = timeit ( "quicksort ( equal_list )" , number =1000 , globals = globals ()) #EQUAL
t4_quick = timeit ( "quicksort ( reversed_list )" , number =1000 , globals = globals ()) #REVERSED

print("RANDOM TIME FOR QUICK: ", t1_quick)
print("SORTED TIME FOR QUICK: ", t2_quick)
print("EQUAL TIME FOR QUICK: ", t3_quick)
print("REVERSED TIME FOR QUICK: ", t4_quick)
