class Stack : 
    data = []
    
    def __init__(self,data = []):
            self.data = data.copy()
           
    def Count(self):
        return len(self.data)
          
    def Push(self ,value):
        self.data.append(value)
   
    def Pop (self):
        if self.count() > 0:
            return self.data.pop(-1)
        return None
    
    def Top (self):
        if self.count():
            return self.data[len[self.data]-1]
    
    def IsEmpty(self):
        return len(self.data) == 0 

    def __add__(self, other : any ):        
        self.data +=  other.data
        
    def __str__(self): 
        str_to_print ='';
        for  i in self.data[::-1]:
            str_to_print = str_to_print + '=> ' +  i 
        print (str_to_print)
        
        
        




         
    