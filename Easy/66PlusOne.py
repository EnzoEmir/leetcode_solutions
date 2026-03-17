# class Solution(object):
#     def plusOne(self, digits):
#         ultimo = len(digits) - 1
#         digits[ultimo] += 1 
#         for x in range(ultimo, 0, -1):
#             if digits[x] == 10:
#                 digits[x] = 0
#                 digits[x-1] += 1
#         if digits[0] == 10:
#             digits[0] = 0
#             return [1] + digits

#         return digits 


class Solution(object):
    def plusOne(self, digits):
        ultimo = len(digits) - 1
        for x in range(ultimo, -1, -1):
            if digits[x] < 9:
                digits[x] += 1
                return digits

            digits[x] = 0

        return [1] + digits 
