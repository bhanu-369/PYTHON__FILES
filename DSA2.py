#CIRCLE LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class C:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("empty")
        temp=self.head
        print(temp.data)
        while temp.next!=self.head:
            print(temp.data)
            
obj=C()
n=Node(10)
obj.head=n
obj.tail=n
obj.tail.next=obj.head
print(" 1st element")

n1=Node(20)
obj.tail.next=n1
obj.tail=n1
obj.tail=obj.head

        
