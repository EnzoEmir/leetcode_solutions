class Solution(object):
    def removeElement(self, nums, val):
        posicao = 0

        for x in range(len(nums)):
            if nums[x] != val:
                nums[posicao] = nums[x]
                posicao += 1
        
        return posicao
    