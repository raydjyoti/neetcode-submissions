class TimeMap:

    def __init__(self):
        self.timeMap = dict()
        self.keys = dict()


    def set(self, key: str, value: str, timestamp: int) -> None:
        customKey = f"{key}-{timestamp}"
        self.timeMap[customKey] = value

        if (key in self.keys):
            stack = self.keys[key]
            stack.append(timestamp)
            self.keys[key] = stack

        else: self.keys[key] = [timestamp]


    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.keys): return ""


        customKey = f"{key}-{timestamp}"
        

        if (customKey in self.timeMap): return self.timeMap[customKey]
        else:
            stack = self.keys[key]
            left = 0
            right = len(stack)-1

            while (left <= right):
                mid = (left+right) // 2
                midVal = stack[mid]
                leftVal = stack[left]
                rightVal = stack[right]

                if (midVal > timestamp): right = mid-1
                elif (midVal < timestamp): left = mid+1

            if right < 0: return ""
            nextSmallest  = stack[right]
 
            customKey = f"{key}-{nextSmallest}"
            return self.timeMap[customKey]

            




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)