class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = sorted(nums1 + nums2)
        if len(merged_array) % 2 != 0:
            median = len(merged_array) // 2
            return merged_array[median]
        else:
            median = merged_array[(len(merged_array) // 2) - 1] + merged_array[len(merged_array) // 2]
            return median/2.0