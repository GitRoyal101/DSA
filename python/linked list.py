class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
        nnode=Node(data)
        if not self.head:
            self.head=nnode
            return
        current=self.head
        while(current.next):
            current=current.next
        current.next=nnode
    def display(self):
        current=self.head
        while current:
            print(current.data,"-->",end="")
            current=current.next
        
#creating the linked list
ll=linkedlist()
ll.add(1)
ll.add(2)
ll.add(3)

#display the linked list
ll.display()
