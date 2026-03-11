class Solution(object):
    def searchInsert(self, nums, target):
        esquerda = 0
        direita = len(nums) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2

            if nums[meio] == target:
                return meio
            
            if nums[meio] > target:
                direita = meio -1

            else:
                esquerda = meio + 1
            
        return esquerda
        