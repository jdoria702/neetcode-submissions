class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from right to left
        # Store the greater number nums1[p1], nums2[p2] into nums1[p3]
        # Decrement p1 or p2
        # Decrement p3
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1

        # exhaust the shorter list
        while p3 >= 0 and p2 >= 0 and p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 = p1 - 1
            else:
                nums1[p3] = nums2[p2]
                p2 = p2 - 1
            p3 = p3 - 1
        
        # add remaining values of larger list
        # num2 has remaining values:
        if p1 == -1:
            for i in range(p2, -1, -1):
                nums1[p3] = nums2[i]
                p3 = p3 - 1
        # num1 has remaining values
        elif p2 == -1:
            for i in range(p1, -1, -1):
                nums1[p3] = nums1[i]
                p3 = p3 - 1

