class Solution(object):
    def permute(self, nums):
        permutations_object =itertools.permutations(nums)
        permutations_list = list(permutations_object)
        return  permutations_list