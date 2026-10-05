class TimeMap:

    def __init__(self):
        self.array = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.array:
            self.array[key] = []
        
        self.array[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.array:
            return ""

        l = 0
        r = len(self.array[key]) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if self.array[key][mid][0] == timestamp:
                return self.array[key][mid][1]
            elif timestamp > self.array[key][mid][0]:
                l = mid + 1
            else:
                r = mid - 1
        
        if r == -1:
            return ""

        return self.array[key][r][1]       
