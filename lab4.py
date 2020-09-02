class Stack:

    class Node:

        def __init__(self,value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.ptr = None
    

    def  insert(self,value):

        newNode = self.Node(value)
        if(self.ptr == None):
            self.ptr = newNode
        else : 
            self.ptr.next = newNode
            newNode.prev = self.ptr
            self.ptr = newNode

    def pop(self):
        
        self.ptr = self.ptr.prev
        self.ptr.next = None
        return self.ptr.value

    def top(self):
        return self.ptr.value

    def empty(self):
        return True if self.ptr == None else False

    def print(self):
        lst = []
        ptr = self.ptr 
        while (ptr != None):
            print(ptr.value,end=" ")
            lst.append(ptr.value)
            ptr = ptr.prev
        return lst


st = Stack()
print(st.empty())
st.insert(1)
st.insert(2)
st.insert(3)
st.print()
print(st.empty())
st.pop()
st.print()
