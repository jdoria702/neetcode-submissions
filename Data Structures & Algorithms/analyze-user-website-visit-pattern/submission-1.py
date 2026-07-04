class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # sort websites by timestamp
        # TC: O(n)
        # SC: O(n)
        sort_time = []
        for i in range(len(username)):
            sort_time.append((timestamp[i], website[i], username[i]))
        sort_time.sort()

        # group entries by user
        # key: username
        # value: [list of websites]
        # TC: O(n)
        # SC: O(n)
        hmap_user = {}
        for group in sort_time:
            if group[2] not in hmap_user:
                hmap_user[group[2]] = []

            hmap_user[group[2]].append(group[1])
        
        # count frequencies per user.. use a set so that each combination is unique and not recounted
        count = {}
        for k, v in hmap_user.items():
            s = set()
            for i in range(len(v) - 2):
                tup = tuple(v[i:i+3])
                if tup not in s:
                    s.add(tup)
                    count[tup] = count.get(tup, 0) + 1

        best = None

        for pattern in count:
            if best is None:
                best = pattern
            elif count[pattern] > count[best]:
                best = pattern
            elif count[pattern] == count[best] and pattern < best:
                best = pattern

        return list(best)