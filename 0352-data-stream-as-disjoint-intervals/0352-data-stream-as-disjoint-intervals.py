class SummaryRanges:

    def __init__(self):
        self.arr = []
        self.sets  = []
        

    def addNum(self, value: int) -> None:
        self.arr.append(value)
        #print(self.arr)
        
        if (not len(self.sets) ) or  ( len(self.sets) and value < self.sets[0][0] -1 ):
                # if value is going to be 1st set 
                self.sets.insert(0,[value,value])
                #print(self.sets)
                return
            
        if value > self.sets[len(self.sets) - 1 ][1] + 1 :
                # if value is going to be last set 
                self.sets.append([value,value])
                #print(self.sets)
                return
        if value == self.sets[len(self.sets) - 1 ][1] + 1 :
                # if value is going to be last set 
                self.sets[len(self.sets) - 1 ][1] = value
                #print(self.sets)
                return
            
        for i in range(len(self.sets)):
            if  self.sets[i][0] <= value <= self.sets[i][1]:
                #print(self.sets)
                return
            elif self.sets[i][1] + 1 < value < self.sets[i+1][0] - 1:
                self.sets.insert(i + 1,[value,value])
                #print(self.sets)
                return
            elif self.sets[i][1] + 1 == value == self.sets[i+1][0] - 1:
                next_set = self.sets.pop(i + 1)
                self.sets[i][1] = next_set[1]
                #print(self.sets)
                return
            elif self.sets[i][1] + 1 == value:
                self.sets[i][1] = value
                #print(self.sets)
                return
            elif self.sets[i][0] - 1 == value:
                self.sets[i][0] = value
                #print(self.sets)
                return
                
            
        

    def getIntervals(self) -> List[List[int]]:
        return self.sets
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()