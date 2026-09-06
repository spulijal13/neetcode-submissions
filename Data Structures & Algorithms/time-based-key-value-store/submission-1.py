class TimeMap:

    def __init__(self):
        self.timeStruct = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStruct:
            self.timeStruct[key] = []
        
        self.timeStruct[key].append((timestamp, value))
        print(self.timeStruct)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeStruct:
            return ""
        
        start = 0
        end = len(self.timeStruct[key]) - 1

        while start <= end:
            mid = (start + end) // 2
            
            if self.timeStruct[key][mid][0] == timestamp:
                return self.timeStruct[key][mid][1]
            elif self.timeStruct[key][mid][0] > timestamp:
                end = mid - 1
            else:
                start = mid + 1
        
        print(start, end)
        if end < 0:
            return ""
        return self.timeStruct[key][end][1]
        
