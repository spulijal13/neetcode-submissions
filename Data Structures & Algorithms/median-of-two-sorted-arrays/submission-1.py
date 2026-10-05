class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l = 0
        r = len(nums1)
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        while l <= r:
            p1 = (l + r) // 2
            p2 = half - p1

            left1 = float("-inf") if (p1 <= 0) else nums1[p1 - 1]
            right1 = float("inf") if (p1 >= len(nums1)) else nums1[p1]
            left2 = float("-inf") if (p2 <= 0) else nums2[p2 - 1]
            right2 = float("inf") if (p2 >= len(nums2)) else nums2[p2]

            if left1 > right2:
                r = p1 - 1
            elif left2 > right1:
                l = p1 + 1
            else:
                break
        
        if total % 2 == 0:
            return (min(right1, right2) + max(left1, left2)) / 2
        else:
            return max(left1, left2)

            