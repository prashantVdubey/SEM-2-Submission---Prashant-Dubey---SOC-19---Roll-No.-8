class stack : 
    def __init__(self) : 
        self.stack = []
        
    def push(self, item ): 
        self.stack.append(item)
        print ( item, " pushed into stack ")
         
    def safe_pop(self):
        if len ( self.stack)==0:
            print ("stack is empty ,nothing to pop .")
            return None 
        else :
            return self.stack.pop()
                
    def display (self): 
        print ("stack element : ",self.stack ) 
s = stack()
            
while True : 
    print ("\n1. push ")    
    print ("2. pop ")
    print ("3. Display  ")
    print ("4. Exit ")
        
    choice = int ( input ( " enter your choice :  "))
        
    if choice ==1 : 
        item = int ( input (" enter a element to push :"))
        s.push( item )
        
    elif choice ==2 :
        result = s.safe_pop()
        print ("popped element :" ,result)
        
    elif choice == 3 : 
        s.display ()
        
    elif choice == 4 : 
        print ("exiting program ... ")
        
    else : 
        print ("invalid choice ! try again .")
