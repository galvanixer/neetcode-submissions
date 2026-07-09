class Solution:

    def encode(self, strs: List[str]) -> str:
        strsout: list[str] = []
        for s in strs:
            strsout.append(str(len(s)))
            strsout.append("#")
            strsout.append(s)

        return "".join(strsout)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            lenstring = int(s[i:j])
            i = j+1
            j = i+lenstring
            res.append(s[i:j])
            i=j

        return res
