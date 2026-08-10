class TimeMap:

    def __init__(self):
        self.kvstore = {} # key -> (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvstore:
            self.kvstore[key] = []
        self.kvstore[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.kvstore:
            return ""

        nitems = len(self.kvstore[key])
        left, right = 0, nitems

        while left < right:
            mid = left + (right - left)//2

            if self.kvstore[key][mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1

        if left < 1:
            return ""
        else:
            return self.kvstore[key][left-1][1]


        

        
