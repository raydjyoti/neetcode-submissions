class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        char = ""

        for str in strs:
            encoded += str
            size = len(str)
            char += chr(size)

        return f"{len(char)}{char}{encoded}"

    def decode(self, s: str) -> List[str]:
        decoded = []
        currStr = ""

        c = 1

        # "43459ateballdance"

        startIndex = int(s[0])+1

        for i in range(int(s[0])):
            char = s[c]
            count = ord(char)

            print(count)

            for j in range(startIndex, startIndex+count):
                currStr += s[j]

            decoded.append(currStr)
            currStr = ""
            startIndex += count
            c+=1

        return decoded








