class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        # Store pairs of (sorted_string, original_string) to keep track of original values
        pairs = []
        for s in strs:
            pairs.append(("".join(sorted(s)), s))
        
        # Sort the pairs based on the sorted_string key
        pairs.sort()

        result = []
        l = 0
        r = 1
        while r < len(pairs):
            if pairs[l][0] == pairs[r][0]:
                r = r + 1
            else:
                # Extract original strings from the pair range
                result.append([p[1] for p in pairs[l:r]])
                l = r
                r = r + 1

        result.append([p[1] for p in pairs[l:r]])
        return result