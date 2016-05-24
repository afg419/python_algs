import random

class MergeSort:
    def __init__(self, array):
        self.array = array

    def sort_2_sorted(self, a1, a2):
        i, j, sorted_a = 0, 0, []
        for element in enumerate(a1 + a2):
            if (len(a1) <= i or len(a2) <= j):
                return sorted_a + a1[i:len(a1)] + a2[j:len(a2)]
            elif a1[i] < a2[j]:
                sorted_a.append(a1[i])
                i += 1
            else:
                sorted_a.append(a2[j])
                j +=1

    def merge_sort(self, array):
        if len(array) == 1:
            return array
        else:
            left, right = array[0:len(array)/2], array[(len(array)/2):len(array)]
            # import pdb; pdb.set_trace()
            return self.sort_2_sorted(self.merge_sort(left), self.merge_sort(right))

ms = MergeSort([1,2,3])
print ms.array

print ms.sort_2_sorted([2,4,6], [3,5,7])
print ms.sort_2_sorted([1,2,3], [3,5,7])
print ms.sort_2_sorted([1,2,3], [4,5,6])
print ms.sort_2_sorted([4,5,6], [1,2,3])
print ms.merge_sort([1,2,3,4,5,6])
print ms.merge_sort([6,5,4,3,2,1])
print ms.merge_sort([6,2,4,3,1,1,7])
