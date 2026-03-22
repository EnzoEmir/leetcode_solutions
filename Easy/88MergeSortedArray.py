class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ult1 = m - 1
        ult2 = n - 1

        final = m + n - 1

        while ult1 >= 0 and ult2 >= 0:
            if nums1[ult1] >= nums2[ult2]:
                nums1[final] = nums1[ult1]
                ult1 -= 1
            
            else:
                nums1[final] = nums2[ult2]
                ult2 -= 1
            final -= 1

        while ult2 >= 0:
            nums1[final] = nums2[ult2]
            ult2 -= 1
            final -= 1
        