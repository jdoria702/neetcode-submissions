class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Create list of tuples (sorted_string, original_string)
        Iterate through array and group tuples that have the same sorted_string
        Extract the original_string from each group and add to list
        When new word is met, add current list to result and reset it
        """

        hmap = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            hmap[sorted_s] = hmap.get(sorted_s, []) + [s]

        res = []
        for _, v in hmap.items():
            res.append(v)

        return res  