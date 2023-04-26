from abc import ABC, abstractmethod


class Sorter(ABC):

    @abstractmethod
    def sort(self):
        raise NotImplementedError


class BubbleSort(Sorter):
    
        def sort(self):
            print("Bubble sort")


class QuickSort(Sorter):

    def sort(self):
        print("Quick sort")


class MergeSort(Sorter):
    
        def sort(self):
            print("Merge sort")


class SorterContext:

    def __init__(self, sorter: Sorter):
        self._sorter = sorter

    def sort(self):
        self._sorter.sort()
        