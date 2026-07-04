class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ##############################################################################
        
        # ALGORITHM:
        # Sort by start
        # Overlap occurs when between two lists (l1 and l2) when:
            # make sure l1 has the smaller starting point
            # l1[0] <= l2[0] <= l2[1]
        # If there is overlap, modify the end to be the larger value
        # If no overlap, append the second interval in the result array

        ##############################################################################

        # TC: O(nlogn)
        intervals.sort()

        res = []
        res.append(intervals[0])
        for start, end in intervals[1:]:
            last = res[-1]
            if start <= last[1]:
                last[1] = max(end, last[1])
            else:
                res.append([start, end])
        return res