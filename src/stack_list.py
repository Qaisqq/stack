class StackList:
    def __init__(self): 
        self.list = []
    
    def push(self, data): #the push'd data will always be index 0
        self.list[:0] = [data]