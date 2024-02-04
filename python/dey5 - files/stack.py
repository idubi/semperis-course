class Stack : 
    data = []
    
    def __init__(self,*args):
        for arg in args:
             self.data.push(arg)
           
    def count(self):
        return len(self.data)
          
    def push(self ,value):
        self.data.push(-1)
        return len(self.data)
   
    def pop (self):
        if self.count() > 0:
            return self.data.pop()
    
    def top (self):
        if self.count()
    
    def add(self, other : any ):
        
        pass
         
    