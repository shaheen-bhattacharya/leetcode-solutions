class MyCalendarThree:
    def __init__(self):
        self.prev = 0
        self.events = SortedList()

    def book(self, startTime: int, endTime: int) -> int:
        self.events.add((startTime, 1))
        self.events.add((endTime, -1))
        curr = 0
        res = 0
        for i in range(len(self.events)):
            if self.events[i][1] == 1:
                curr += 1
                res = max(res, curr)
            else:
                curr -= 1
        return res




# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)