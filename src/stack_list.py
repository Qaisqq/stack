class StackList:
    def __init__(self): 
        self.list = []  

    def push(self, data): #the push'd data will always be index 0
        self.list[:0] = [data]

    def pop(self):
        if self.is_empty(): ##check if empty
            return None
        temp = self.list[0]
        self.list = self.list[1:] #create a new list from index1 to the end
        return temp    #assign new list to old list, and return temp value

    def is_empty(self): #if self.list is empty, it returns as false
        return not self.list #we use not, to reverse the boolean to true