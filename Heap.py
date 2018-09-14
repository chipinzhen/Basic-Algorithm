class Heap(object):
    
    def __init__(self, list_1, capacity, isMaxHeap = True):
        self.capacity = capacity
        self.heap = list_1
        self.account = len(list_1)
        
    def shiftUp(self, value):
        self.account += 1
        if self.account // 2 == 0:
            self.heap.append(value)
        else:
            self.heap.append(value)
            index = self.account
            while(index // 2 > 0):
                if self.heap[index - 1] > self.heap[index//2 - 1] :
                    temp = self.heap[index - 1]
                    self.heap[index - 1] = self.heap[index//2 - 1]
                    self.heap[index//2 - 1] = temp
                    index = index // 2
                else:
                    break
        
    
    def popMax(self):
        
        
        if self.account > 0:
            pop_value = self.heap[0]

            self.heap[0] = self.heap[self.account - 1]
            self.account -= 1
            self.heap.pop()
        
            i = 0
            while(2 * i + 1 + 1 <= self.account):

                if 2 * i + 3 <= self.account:

                    if (self.heap[2 * i + 1] >= self.heap[2 * i + 2]) & (self.heap[2 * i + 1] > self.heap[i]):

                        temp = self.heap[i] 
                        self.heap[i] = self.heap[2 * i + 1]
                        self.heap[2 * i + 1] = temp
                        i = 2 * i + 1

                    if (self.heap[2 * i + 1] < self.heap[2 * i + 2]) & (self.heap[2 * i + 2] > self.heap[i]):

                        temp = self.heap[i] 
                        self.heap[i] = self.heap[2 * i + 2]
                        self.heap[2 * i + 2] = temp
                        i = 2 * i + 2

                else:

                    if self.heap[2 * i + 1] > self.heap[i]:
                        temp = self.heap[i] 
                        self.heap[i] = self.heap[2 * i + 1]
                        self.heap[2 * i + 1] = temp
                        i = 2 * i + 1
                    
        
        
    def shiftDown(self, pos):
        
        if pos < self.account:
            
            i = pos
            while(2 * i + 1 + 1 <= self.account):

                if 2 * i + 3 <= self.account:

                    if (self.heap[2 * i + 1] >= self.heap[2 * i + 2]) & (self.heap[2 * i + 1] > self.heap[i]):

                        temp = self.heap[i] 
                        self.heap[i] = self.heap[2 * i + 1]
                        self.heap[2 * i + 1] = temp
                        i = 2 * i + 1

                    elif (self.heap[2 * i + 1] < self.heap[2 * i + 2]) & (self.heap[2 * i + 2] > self.heap[i]):

                        temp = self.heap[i] 
                        self.heap[i] = self.heap[2 * i + 2]
                        self.heap[2 * i + 2] = temp
                        i = 2 * i + 2
                    
                    elif (self.heap[2 * i + 2] < self.heap[i]) & (self.heap[2 * i + 1] < self.heap[i]):
                        break

                else:

                    if self.heap[2 * i + 1] > self.heap[i]:
                        temp = self.heap[i] 
                        self.heap[i] = self.heap[2 * i + 1]
                        self.heap[2 * i + 1] = temp
                        i = 2 * i + 1
                    else:
                        break
    
    
    
    def heapify(self):
        
        for i in range(self.account // 2, 0, -1):
            pos = i - 1
            self.shiftDown(pos)
        return self.heap
                    
            
        
        
    
    