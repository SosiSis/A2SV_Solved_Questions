class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.counter=0
        self.queue=deque()
        

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num==self.value:
            self.counter+=1
 
        if len(self.queue) > self.k:
            removed =self.queue.popleft()
            if removed == self.value:
                self.counter-=1    
        return self.k ==self.counter


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)