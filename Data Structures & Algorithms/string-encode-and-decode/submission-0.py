class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        nums = ""

        for str in strs:
            encoded += str
            nums += f"{len(str)}"

        return f"{len(nums)}{nums}{encoded}"

    def decode(self, s: str) -> List[str]:
        decoded = []
        currStr = ""

        c = 1

        # "43459ateballdance"


        startIndex = int(s[0])+1

        for i in range(int(s[0])):
            count = int(s[c])

            for j in range(startIndex, startIndex+count):
                currStr += s[j]

            decoded.append(currStr)
            currStr = ""
            startIndex += count
            c+=1

        return decoded








