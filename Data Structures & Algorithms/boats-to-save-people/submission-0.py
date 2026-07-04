class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort
        # [1, 2, 4, 5]
        # 2 pointer - start and end
        # Try matching a heavy person with a light person
        # if you cant:
            # heavy person must have boat to themselves
            # else pair them
        # increment/decrement pointers and repeat

        # [1, 2, 2, 3, 3]
        # 3 self
        # self
        # 1 and 2
        # 2

        # edge case: pointers match
        # [1, 2, 1]; limit=2
        # pair 1, 1
        # check at end if l == r
        # make an extra boat if so


        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l < r:
            if people[l] + people[r] <= limit:
                count = count + 1
                l = l + 1
                r = r - 1
            else:
                count = count + 1
                r = r - 1
        if l == r:
            count = count + 1
        return count