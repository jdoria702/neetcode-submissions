class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Split array in half
        # Recursive split until size of array is empty
        # Merge left array and right array
        
        def mergesort(arr):
            print("arr: ", arr)
            if len(arr) == 0:
                return []
            
            if len(arr) == 1:
                return arr
            
            # split array in half
            half = len(arr) // 2
            print("split: ", arr[:half], arr[half:])
            print("calling left", arr[:half])
            left = mergesort(arr[:half])
            print("calling right with: ", arr[half:])
            right = mergesort(arr[half:])

            print("left: ", left)
            print("right: ", right)

            # sort
            ret = []
            ptr1 = 0
            ptr2 = 0
            while left and right and ptr1 < len(left) and ptr2 < len(right):
                if left[ptr1] < right[ptr2]:
                    ret.append(left[ptr1])
                    ptr1 = ptr1 + 1
                else:
                    ret.append(right[ptr2])
                    ptr2 = ptr2 + 1

            # append remaining
            if ptr1 == len(left):
                ret = ret + right[ptr2:]
            else:
                ret = ret + left[ptr1:]

            print("Returning: ", ret)
            return ret

        ans = mergesort(nums)
        return ans