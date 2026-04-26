from collections import deque 

class queue :
    def _init_(self):
        self.queue = deque()

    def enqueue (self ,item ):
        self.queue.append (item )
        print(item,"added to queue ") 
    def safe_dequeue (self):
            if len (self.queue )== 0 : 
                print ("Queue is empty , cannot dequeue .")
                return None 
            else : 
                return self.queue.popleft()
    def display ( self ):
        print (" Queue elements : ", list (self .queue ))
        
q = queue()
while True :
    print ("\n1. enqueue")
    print ("2.dequeue ")
    print ("3.display")
    print ("4 . Exit ")
    
    choice = int (input ("enter your choice : "))
    if choice ==1 :
        item = int (input ("enter element to enqueue:  "))
        q.enqueue(item )
        
    elif choice == 2: 
        result = q.safe_dequeue()
        print ("dequeue element: ", result )
 
    elif choice == 3 : 
        q.display ()  
        
    elif choice == 4 : 
        print (" Exiting program ... ") 
        break 
     
    else : print ("Invalid choice ! Try again . ")
