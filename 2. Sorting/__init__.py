# Pozostaw ten plik pusty, ew. wykorzystaj do własnych testów.

import unittest
from sort import quicksort
from sort import bubblesort
import random

class TestSorting(unittest.TestCase):
    def test_quicksort1(self):
        lst = [2, 25, 9, 14, 1, 3, 10]
        self.assertListEqual(quicksort(lst), [1, 2, 3, 9, 10, 14, 25])

    def test_bubblesort1(self):
        lst = [2, 25, 9, 14, 1]
        self.assertEqual(bubblesort(lst), ([1, 2,  9,  14, 25], 10))

    def test_bubblesort2(self):
        lst = [2, 30, 15, 2, 20, 21, 50, 55, 100, 27, 99, 30]
        self.assertEqual(bubblesort(lst), ([2, 2, 15, 20, 21, 27, 30, 30, 50, 55, 99, 100], 66))


