"""class doublestack:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.mid=(n+1)//2
        self.top1=-1
        self.top2=self.mid-1
    def push(self,data):
        if self.top1<self.mid-1:
            self.top1+=1
            self.arr[self.top1]=data
            print("pushed(data) into stack")
        else:
            print("Stack is Overfiow")
    def push2(self,data ):
        if self.top2<self.size-1:
            self.top2+=1
            self.arr[self.top2]=data
            print("pushed2 (data) into stack")
        else:
            print("stack is Overflow")
    def pop(self):
        if  self.top1>=0:
            print("Empty")
            data=self.arr[self.top1]
            self.arr[self.top1]=None
            self.top1-=1
            print(f"popped {data} from stack1")
            return data
        else:
            print("Stack underflow")
            return None
    def pop1(self):
        if self.top2>=self.mid:
            data=self.arr[self.top2]
            self.arr[self.top2]=None
            self.top2-=1
            print(f"pop {data} from Stack2")
        else:
            print("Stack underflow")
            return None
    def display(self):
        print(f"Array :{self.arr}")
        print(f"Stack1:{self.arr[:self.mid]}")
        print(f"Stack2 :{self.arr[self.mid:]}")
obj=doublestack(5)
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.display()
"""
class TwoStack:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*size
        self.top1=-1
        self.top2=size
        






           
        
            
