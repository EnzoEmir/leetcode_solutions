class Solution(object):
    def removeDuplicates(self, nums):
        contador  = 0
        for x in range(len(nums)):
            if nums[x] > nums[contador]:
                contador += 1

                nums[contador] = nums[x]
        return contador + 1
