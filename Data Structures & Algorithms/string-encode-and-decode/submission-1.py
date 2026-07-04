class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        l = 0
        r = 1
        while r < len(s):
            # Find the length of the word
            if s[r] != '#':
                r = r + 1
                continue
            else:
                length = int(s[l:r])
            
            # read up to (length) characters and append to result
            result.append(s[r+1:r+1+length])
            l = r + 1 + length
            r = l + 1
            
        return result