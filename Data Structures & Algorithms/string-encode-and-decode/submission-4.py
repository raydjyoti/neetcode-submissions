class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for str in strs:
            encoded += f"#{len(str)}{str}"
        return encoded

    def decode(self, s: str) -> List[str]:

        output = []

        i = 0

        while (i < len(s)):

            sLen = int(s[i+1])
            string = s[i+2:sLen+i+2]
            output.append(string)
            i = sLen+i+2

        return output







