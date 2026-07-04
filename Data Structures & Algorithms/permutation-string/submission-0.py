class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        have = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1
        
        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1) - 1

        for i in range(r):
            have[s2[i]] = have.get(s2[i], 0)  + 1

        while r < len(s2):
            have[s2[r]] = have.get(s2[r], 0) + 1
            match = 0
            # Is the current window valid?
            for need_k, need_v in need.items():
                if have.get(need_k) == need_v:
                    match = match + 1
                if match == len(need):
                    return True
            
            have[s2[l]] = have[s2[l]] - 1
            l = l + 1
            r = r + 1

        return False