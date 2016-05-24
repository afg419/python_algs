class RadixSort:
    def radix_sort(self, array):
        longest_key = len(str(max(array, key=lambda elt:len(str(elt)))))
        for i in range(1, longest_key+1):
            array = self.place_to_buckets(array, i)
        return array

    def place_to_buckets(self, array, index):
        buckets = map(lambda i : [], range(0,9))
        for elt in array:
            buckets[self.get_digit(elt, index)].append(elt)
        return sum(buckets, [])

    def get_digit(self, num, index):
        lead, fol = 10**index, 10**(index-1)
        return (num % lead - num % fol)/fol





rs = RadixSort()
print rs.radix_sort([1,2,3,4])
print rs.radix_sort([2,1,3,4])
print rs.radix_sort([2,1,2,4])
print rs.radix_sort([23,31,111,4])
#
# print rs.place_to_buckets([123, 234, 122, 335], 2)
# print rs.place_to_buckets([123, 234, 122, 335], 1)
# print rs.place_to_buckets([123, 234, 122, 335], 3)
#
# print rs.get_digit(12345,1)
# print rs.get_digit(12345,2)
# print rs.get_digit(12345,3)
# print rs.get_digit(12345,4)
# print rs.get_digit(12345,5)
# print rs.get_digit(1,5)
