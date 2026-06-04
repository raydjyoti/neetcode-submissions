class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for str in strs:
            encoded += f"{len(str)}#{str}"
        return encoded

    def decode(self, s: str) -> List[str]:

        output = []
        i = 0
        count = ""

        while (i < len(s)):

            if (s[i] == "#"):
                sLen = int(count)
                count = ""
                string = s[i+1:sLen+i+1]
                output.append(string)
                i = i+1+sLen

            else:
                count+= s[i]
                i+=1

        return output







