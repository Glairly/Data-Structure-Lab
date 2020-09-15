# # simply
# class LinkedList:

#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.next = None
#             self.prev = None

#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __str__(self):
#         ptr = self.head
#         result = []
#         while(ptr != None):
#             result.append(ptr.data)
#             ptr = ptr.next
#         return result

#     def append(self, value):
#         newNode = self.Node(value)

#         if(self.head == None):
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             newNode.prev = self.tail
#             self.tail = newNode

#     def insert(self, index, value):


#         if(index < 0):
#             return False

#         if(self.isEmpty() and index == 0):
#             self.append(value)
#             return True
#         if(self.isEmpty() and index > 0):
#             return False

#         ptr = self.head
#         count = 0
#         newNode = self.Node(value)

#         if (index == 0): # rebase
#             newNode.next = self.head
#             self.head.prev = newNode
#             self.head = newNode
#             return True

#         while(ptr != None and count < index - 1):
#             if(ptr.next == None):
#                 break
#             ptr = ptr.next
#             count += 1

#         if(count < index-1):
#             return False


#         newNode.next = ptr.next
#         ptr.next = newNode
#         newNode.prev = ptr

#         return True


#     def isEmpty(self):
#         if(self.head == None):
#             self.tail = None
#         return self.head == None

#     def pop(self,index = -1):
#         value = ""
#         if(index == -1):
#             value = self.tail.data
#             self.tail = self.tail.prev
#             self.tail.next = None
#         else:
#             ptr = self.head
#             count = 1
#             if(ptr == None):
#                 return  False
#             while(ptr != None and count != index):
#                 count += 1
#                 if(ptr.next == None):
#                     break
#                 ptr = ptr.next

#             if(count < index):
#                 return False


#             temp_p = ptr.prev
#             temp_n = ptr.next

#             if (temp_n != None):
#                 temp_n.prev = temp_p
#             if (temp_p != None):
#                 temp_p.next = temp_n

#             if(ptr == self.head):
#                 self.head = self.head.next
#             elif(ptr == self.tail):
#                 self.tail = self.tail.prev

#         return value


# ll = LinkedList()

# x = input("Enter Input : ")

# x = x.split(',')

# for i in x[0].split():
#     ll.append(i)

# if(len(ll.__str__()) > 0):
#     print("link list : ",end="")
#     print(*ll.__str__(),sep="->")
# else:
#     print("List is empty")

# for i in range(1,len(x)):

#     index,value = x[i].split(':')

#     isAddable = ll.insert(int(index),int(value))
#     if(isAddable):
#         print("index =",int(index),"and data =",value)
#     else:
#         print("Data cannot be added")

#     if(not ll.isEmpty()):
#         print("link list : ",end="")
#         print(*ll.__str__(),sep="->")
#     else:
#         print("List is empty")


# douply
class LinkedList:
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None


    def command(self,command,value):
        if(command == "I"):
            index,value = value.split(":")
            isAddable = self.func["I"](index,value)
            if(isAddable):
                print("index =",int(index),"and data =",value)
            else:
                print("Data cannot be added")
        elif(command == "Ab"):
            index,value = 0,value
            return self.func["Ab"](index,value)
        elif(command == "R"):
            index,value = self.func["R"](value)
            if(value):
                print("removed :",value,"from index :",index)
            else:
                print("Not Found!")
        else:
            return self.func[command](value)

    def __init__(self):
        self.head = None
        self.tail = None
        self.func = {
            "A"  : self.append,
            "Ab" : self.insert,
            "I"  : self.insert,
            "R"  : self.remove
        }

    def __str__(self):
        ptr = self.head
        result = []
        while(ptr != None):
            result.append(ptr.data)
            ptr = ptr.next
        return result

    def str_reverse(self):
        ptr = self.tail
        result = []
        while(ptr != None):
            result.append(ptr.data)
            ptr = ptr.prev
        return result

    def append(self, value):
        newNode = self.Node(value)

        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def insert(self, index, value):
        index,value = int(index),int(value)
        if(index < 0):
            return False

        if(self.isEmpty() and index == 0):
            self.append(value)
            return True
        if(self.isEmpty() and index > 0):
            return False

        ptr = self.head
        count = 0
        newNode = self.Node(value)

        if (index == 0): # rebase
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return True

        while(ptr != None and count < index - 1):
            if(ptr.next == None):
                break
            ptr = ptr.next
            count += 1

        if(count < index-1):
            return False


        newNode.next = ptr.next
        if(ptr.next != None):
            ptr.next.prev = newNode
        ptr.next = newNode
        newNode.prev = ptr

        while(self.tail != None and self.tail.next != None):
            self.tail = self.tail.next

        while(self.head != None and self.head.prev != None):
            self.head = self.head.prev

        return True


    def isEmpty(self):
        if(self.head == None):
            self.tail = None
        return self.head == None

    def remove(self,data):

        ptr = self.head
        index = 0
        while(ptr != None):
            if(int(ptr.data) == int(data)):

                if(ptr == self.head):
                    self.head = self.head.next
                    if(self.head != None):
                        self.head.prev = None
                    else:
                        self.setEmpty()
                    return index,ptr.data

                if(ptr == self.tail):
                    self.tail = self.tail.prev
                    if(self.tail != None):
                        self.tail.next = None
                    else:
                        self.setEmpty()
                    return index,ptr.data

                temp_p = ptr.prev
                temp_n = ptr.next

                if(temp_p != None):
                    temp_p.next = temp_n
                if(temp_n != None):
                    temp_n.prev =  temp_p

                
                return index,ptr.data
            ptr = ptr.next
            index += 1
        return -1,None

    def setEmpty(self):
            self.head = None
            self.tail = None

ll = LinkedList()

x = input("Enter Input : ")

for i in x.split(","):
    command,value = i.split()

    ll.command(command,value)

    print("linked list : ",end="")
    print(*ll.__str__(),sep="->")
    print("reverse : ",end="")
    print(*ll.str_reverse(),sep="->")


# # mergeOrderList
# class node:
#     def __init__(self,data,next = None ):
#         self.data = data
#         self.next = next
#     def __str__(self):
#         return str(self.data)

# def createList(l=[]):
#     ptr = None
#     root = None
#     for i in l:
#         newNode = node(data = int(i))
#         if(ptr == None):
#             root= newNode
#             ptr = newNode
#         else:
#             ptr.next = newNode
#             ptr = newNode
#     return root


# def printList(H):
#     ptr = H
#     while(ptr != None):
#         print(ptr.data,end=" ")
#         ptr = ptr.next
#     print()

# def mergeOrderesList(p,q):

#     root = None
#     tail = None
#     ptr_L = p
#     ptr_R = q

#     while(ptr_L != None or ptr_R != None):

#         if(ptr_L == None):
#             tail.next  = ptr_R
#             break

#         if(ptr_R == None):
#             tail.next  = ptr_L
#             break

#         if(ptr_L != None and ptr_L.data <= ptr_R.data):
#             if(root == None):
#                 root = ptr_L
#                 tail = root
#             else:
#                 tail.next = ptr_L
#                 tail = ptr_L
#             ptr_L = ptr_L.next
#         elif(ptr_R != None):
#             if(root == None):
#                 root = ptr_R
#                 tail = root
#             else:
#                 tail.next = ptr_R
#                 tail = ptr_R
#             ptr_R = ptr_R.next

#     return root


# #################### FIX comand ####################
# # input only a number save in L1,L2
# L1,L2 = input("Enter 2 Lists : ").split()
# L1 = L1.split(',')
# L2 = L2.split(',')
# LL1 = createList(L1)
# LL2 = createList(L2)
# print('LL1 : ',end='')
# printList(LL1)
# print('LL2 : ',end='')
# printList(LL2)
# m = mergeOrderesList(LL1,LL2)
# print('Merge Result : ',end='')
# printList(m)


# # Vscode is better than VIM for sure
# class LinkedList:

#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.next = None
#             self.prev = None

#     def command(self,value):
#         if(value[0] == "I"):
#             command,value = value.split()
#             self.func[command](value)
#         else:
#             self.func[value]()

#     def __init__(self):
#         self.ptr = self.Node("|")
#         self.func = {
#             "I": self.insert,
#             "L": self.Left,
#             "R": self.Right,
#             "B": self.Backspace,
#             "D": self.Delete
#         }

#     def __str__(self):
#         lst = []
#         ptr = self.ptr
#         while(ptr != None and ptr.prev != None):
#             ptr = ptr.prev

#         while(ptr != None):
#             lst.append(ptr.data)
#             ptr = ptr.next
#         return lst

#     def Left(self):
#         prev = self.ptr.prev
#         next = self.ptr.next

#         if(prev == None):
#             return
#          # re-connect
#         if(prev != None):
#             prev.next = next
#         if(next != None):
#             next.prev = prev

#         # shift left
#         next = prev
#         prev = prev.prev
#         self.ptr.prev = prev
#         self.ptr.next = next
#         if(prev != None):
#             prev.next = self.ptr
#         if(next != None):
#             next.prev = self.ptr


#     def Right(self):
#         prev = self.ptr.prev
#         next = self.ptr.next

#         if(next == None):
#             return
#          # re-connect
#         if(prev != None):
#             prev.next = next
#         if(next != None):
#             next.prev = prev

#         # shift right
#         prev = next
#         next = next.next
#         self.ptr.prev = prev
#         self.ptr.next = next
#         if(prev != None):
#             prev.next = self.ptr
#         if(next != None):
#             next.prev = self.ptr

#     def Backspace(self):
#         if(self.ptr.prev != None):
#             prev = self.ptr.prev
#             if(prev.prev != None):
#                 self.ptr.prev = prev.prev
#                 prev.prev.next = self.ptr
#             else :
#                 self.ptr.prev = None
#         else:
#             pass

#     def Delete(self):
#         if(self.ptr.next != None):
#             next = self.ptr.next
#             if(next.next != None):
#                 self.ptr.next = next.next
#                 next.next.prev = self.ptr
#             else:
#                 self.ptr.next = None
#         else:
#             pass

#     def insert(self,value):
#         newNode = self.Node(value)
#         prev = self.ptr.prev
#         if(prev != None):
#             prev.next = newNode

#         self.ptr.prev = newNode
#         newNode.prev = prev
#         newNode.next = self.ptr

#     def isEmpty(self):
#         if(self.head == None):
#             self.tail = None
#         return self.head == None


#         self.head = None
#         self.tail = None


# ll = LinkedList()

# x = input("Enter Input : ")

# for i in x.split(','):
#     ll.command(i)

# print(*ll.__str__())


# radick sort
# class LinkedList:

#     class Node:
#         def __init__(self, data):
#             self.data = data
#             self.next = None
#             self.prev = None

#     def command(self, command, value):
#         if(command == "I"):
#             index, value = value.split(":")
#             isAddable = self.func["I"](index, value)
#             if(isAddable):
#                 print("index =", int(index), "and data =", value)
#             else:
#                 print("Data cannot be added")
#         elif(command == "Ab"):
#             index, value = 0, value
#             return self.func["Ab"](index, value)
#         elif(command == "R"):
#             index, value = self.func["R"](value)
#             if(value):
#                 print("removed :", value, "from index :", index)
#             else:
#                 print("Not Found!")
#         else:
#             return self.func[command](value)

#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.func = {
#             "A": self.append,
#             "Ab": self.insert,
#             "I": self.insert,
#             "R": self.remove
#         }

#     def __str__(self,sort = False):
#         ptr = self.head
#         result = []
#         while(ptr != None):
#             result.append(int(ptr.data))
#             ptr = ptr.next
#         return result if not sort else sorted(result,reverse=True)

#     def str_reverse(self):
#         ptr = self.tail
#         result = []
#         while(ptr != None):
#             result.append(ptr.data)
#             ptr = ptr.prev
#         return result

#     def append(self, value):
#         newNode = self.Node(value)

#         if(self.head == None):
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             newNode.prev = self.tail
#             self.tail = newNode

#     def insert(self, index, value):
#         index, value = int(index), int(value)
#         if(index < 0):
#             return False

#         if(self.isEmpty() and index == 0):
#             self.append(value)
#             return True
#         if(self.isEmpty() and index > 0):
#             return False

#         ptr = self.head
#         count = 0
#         newNode = self.Node(value)

#         if (index == 0):  # rebase
#             newNode.next = self.head
#             self.head.prev = newNode
#             self.head = newNode
#             return True

#         while(ptr != None and count < index - 1):
#             if(ptr.next == None):
#                 break
#             ptr = ptr.next
#             count += 1

#         if(count < index-1):
#             return False

#         newNode.next = ptr.next
#         if(ptr.next != None):
#             ptr.next.prev = newNode
#         ptr.next = newNode
#         newNode.prev = ptr

#         while(self.tail != None and self.tail.next != None):
#             self.tail = self.tail.next

#         return True

#     def isEmpty(self):
#         if(self.head == None):
#             self.tail = None
#         return self.head == None

#     def remove(self, data):

#         ptr = self.head
#         index = 0
#         while(ptr != None):
#             if(int(ptr.data) == int(data)):

#                 if(ptr == self.head):
#                     self.head = self.head.next
#                     if(self.head != None):
#                         self.head.prev = None
#                     else:
#                         self.setEmpty()
#                     return index, ptr.data

#                 if(ptr == self.tail):
#                     self.tail = self.tail.prev
#                     if(self.tail != None):
#                         self.tail.next = None
#                     else:
#                         self.setEmpty()
#                     return index, ptr.data

#                 temp_p = ptr.prev
#                 temp_n = ptr.next

#                 if(temp_p != None):
#                     temp_p.next = temp_n
#                 if(temp_n != None):
#                     temp_n.prev = temp_p
#                 return index, ptr.data
#             ptr = ptr.next
#             index += 1
#         return -1, None

#     def setEmpty(self):
#         self.head = None
#         self.tail = None

#     def size(self):
#         count = 0
#         ptr = self.head
#         while(ptr != None):
#             count += 1
#             ptr = ptr.next

#         return count


# ll = LinkedList()


# def radixSort(ll):
#     count = 1;
#     exp = 1
#     Max = max(ll.__str__())
#     auxArr = [LinkedList() for i in range(10)]
   
#     ptr = ll.tail
#     negativeArr = LinkedList()
#     print("Round :",count)
#     while(ptr != None):
#         if(int(ptr.data) < 0):
#             negativeArr.append(ptr.data)
#             ptr = ptr.prev
#             continue
#         data = str(ptr.data)
#         raw = data
#         data = data[::-1]
#         if(exp - 1 < len(data)):
#             div = int(data[exp-1])
#         else:
#             div = 0
#         auxArr[div].append(raw)
#         ptr = ptr.prev

#     # negative
#     ptr = negativeArr.tail
#     while(ptr != None):
#         data = str(ptr.data)
#         raw = data
#         data = data[::-1]
#         if(exp - 1 < len(data)):
#             div = int(data[exp-1])
#         else:
#             div = 0
#         auxArr[div].append(raw)
#         ptr = ptr.prev

#     exp += 1
#     for i in range(10):
#         print(i, ":", *auxArr[i].__str__(True))
#     print("------------------------------------------------------------")
#     while(True):
#         if(auxArr[0].size() >= ll.size()):
#                 break
#         count += 1
#         print("Round :",count)
        

#         temp = [LinkedList() for i in range(10)]
#         negativeArr = LinkedList()
#         for i in range(0,10):
#             ptr = auxArr[i].head
#             while(ptr != None):
#                 if(int(ptr.data) < 0):
#                     negativeArr.append(ptr.data)
#                     ptr = ptr.next
#                     continue
#                 ptr = ptr.next

#         for i in range(9,-1,-1):
#             ptr = auxArr[i].head
#             while(ptr != None):
#                 if(int(ptr.data) < 0):
#                     ptr = ptr.next
#                     continue
#                 data = str(ptr.data)
#                 raw = data
#                 data = data[::-1]
#                 if(exp - 1 < len(data) ):
#                     div = int(data[exp-1])
#                 else:
#                     div = 0
#                 temp[div].append(raw)
#                 ptr = ptr.next

#         ptr = negativeArr.head
#         while(ptr != None):
#             data = str(ptr.data)
#             raw = data
#             data = data[::-1]
#             if(exp - 1 < len(data) and data[exp-1] != "-"):
#                 div = int(data[exp-1])
#             else:
#                 div = 0
#             temp[div].append(raw)
#             ptr = ptr.next

#         auxArr = temp
#         for i in range(10):
#             print(i, ":", *auxArr[i].__str__(True))
#         print("------------------------------------------------------------")
#         exp += 1
    
#     return auxArr[0],count


# x = input("Enter Input : ")
# ll = LinkedList()
# for i in x.split():
#     ll.append(i)
# print("------------------------------------------------------------")
# sort,times = radixSort(ll)
# print(times-1,"Time(s)")
# print("Before Radix Sort : ",end="")
# print(*ll.__str__(),sep=" -> ")
# print("After  Radix Sort : ",end="")
# print(*sort.__str__(True),sep=" -> ")