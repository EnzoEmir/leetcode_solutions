class Solution(object):
    def twoSum(self, nums, target):
            vistos = {}  
            
            for i, num in enumerate(nums):  
                diff = target - num  
                
                if diff in vistos:
                    return [vistos[diff], i]
                
                vistos[num] = i
                