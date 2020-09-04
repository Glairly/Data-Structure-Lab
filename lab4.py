 

# มาใช้ queue กันเถอะ ไอเด็กเปรต
# class Queue:
    
    # class Node:

    #     def __init__(self,value):
    #         self.value = value
    #         self.next = None

    # def __init__(self):
    #     self.last = None
    #     self.first = None
    

    # def  insert(self,value):
    #     newNode = self.Node(value)
    #     if(self.first == None):
    #         self.first = newNode
    #         self.last = newNode
    #     else : 
    #         self.last.next = newNode
    #         self.last = newNode

    # def pop(self):
    #     last = self.first
    #     value = self.first.value
    #     self.first = self.first.next
    #     del last
    #     return value

    # def head(self):
    #     return self.first.value

    # def tail(self):
    #     return self.last.value

    # def empty(self):
    #     return True if self.first == None else False

    # def print(self):
    #     lst = []
    #     last = self.first
    #     while (last != None):
    #         # print(last.value,end=", ")
    #         lst.append(last.value)
    #         last = last.next
    #     return lst
# q = Queue()
# dq = Queue()

# x = input("Enter Input : ").split(',')

# for i in x:
#     if(i != "D"):
#         command,value = i.split()
#     else:
#         command = "D"

#     if(command == "E"):
#         q.insert(value)
#         print(*q.print(),sep=", ")
#     elif(command == "D"):
#         if(q.empty()):
#             print("Empty")
#         else:
#             pop = q.pop()
#             dq.insert(pop)
#             print(pop,"<- ",end="")
#             print(*q.print() if not q.empty() else "Empty",sep=", " if not q.empty() else "")
        
# print(*dq.print()if not dq.empty() else "Empty",sep=", " if not dq.empty() else "",end="")
# print(" : ",end="")
# print(*q.print() if not q.empty() else "Empty",sep=", " if not q.empty() else "")



# PSD48
# class Queue:
    
    # class Node:

    #     def __init__(self,value):
    #         self.value = value
    #         self.next = None
    #         self.prev = None

    # def __init__(self):
    #     self.last = None
    #     self.first = None
        

    # def insert(self,value):
    #     newNode = self.Node(value)
    #     if(self.first == None):
    #         self.first = newNode
    #         self.last = newNode
    #     else : 
    #         self.last.next = newNode
    #         newNode.prev = self.last
    #         self.last = newNode
          

    # def pop(self):
    #     if(self.first != None):
    #         value = self.first.value
    #         self.first = self.first.next
    #         if(self.first != None):
    #             self.first.prev = None

    #         if(self.first == None):
    #             self.last = None
    #     else:
    #         return False
    #     return value
    

    # def head(self):
    #     if(self.first != None):
    #         return self.first.value

    # def tail(self):
    #     return self.last.value

    # def empty(self):
    #     return True if self.first == None else False

    # def print(self):
    #     lst = []
    #     last = self.first
    #     while (last != None):
    #         # print(last.value,end=", ")
    #         lst.append(last.value)
    #         last = last.next
    #     return lst
# q = Queue()

# x = input("Enter Input : ").split(',')

 
# def ES(que,value):
#     if(que.empty()):
#         que.insert(["ES",value])
#     else:
#         nQ = Queue()
#         while(not que.empty() and que.head()[0] == "ES"):
#             nQ.insert(que.pop())
#         nQ.insert(["ES",value])
#         while(not que.empty()):
#             nQ.insert(que.pop())
#         return nQ
#     return que

        
# def EN(q,value):
#     q.insert(["EN",value])
#     return q


# for i in x:
#     if(i != "D"):
#         command,value = i.split()
#     else:
#         print(q.pop()[1] if not q.empty() else "Empty")
#         continue

#     dic = {
#         "EN" : EN,
#         "ES" : ES
#     }

#     q = dic[command](q,value)


# # ร้านหนังสือโง่ๆ
# #  
# class Queue:
    
#     class Node:

#         def __init__(self,value):
#             self.value = value
#             self.next = None
#             self.prev = None

#     def __init__(self):
#         self.last = None
#         self.first = None
        

#     def insert(self,value):
#         newNode = self.Node(value)
#         if(self.first == None):
#             self.first = newNode
#             self.last = newNode
#         else : 
#             self.last.next = newNode
#             newNode.prev = self.last
#             self.last = newNode
    
          

#     def pop(self):
#         if(self.first != None):
#             value = self.first.value
#             self.first = self.first.next
#             if(self.first != None):
#                 self.first.prev = None

#             if(self.first == None):
#                 self.last = None
#         else:
#             return False
#         return value
    

#     def head(self):
#         if(self.first != None):
#             return self.first.value

#     def tail(self):
#         return self.last.value

#     def empty(self):
#         return True if self.first == None else False

#     def print(self):
#         lst = []
#         last = self.first
#         while (last != None):
#             # print(last.value,end=", ")
#             lst.append(last.value)
#             last = last.next
#         return lst


# q = Queue()
# dp = {}
# x,y = input("Enter Input : ").split('/')

# for i in x.split():
#     i = int(i)    
#     if i in dp:
#         dp[i] += 1
#     else:
#         dp[i] = 1
    
#     q.insert(i)

# for i in y.split(','):

#     if(i == "D"):
#         pop = q.pop()
#         pop = int(pop)
#         dp[pop] -= 1
        
#     else:
#         _,value = i.split()
#         value = int(value)
#         if value in dp:
#             dp[value] += 1
#         else:
#             dp[value] = 1

#         q.insert(value)


# for i in dp:
#     if(dp[i] > 1):
#         print("Duplicate")
#         exit()
 
# print("NO Duplicate")



 
# เดาใจ : ลาบานูน
# class Queue:
    
#     class Node:

#         def __init__(self,value):
#             self.value = value
#             self.next = None
#             self.prev = None

#     def __init__(self):
#         self.last = None
#         self.first = None
        

#     def insert(self,value):
#         newNode = self.Node(value)
#         if(self.first == None):
#             self.first = newNode
#             self.last = newNode
#         else : 
#             self.last.next = newNode
#             newNode.prev = self.last
#             self.last = newNode
    
          

#     def pop(self):
#         if(self.first != None):
#             value = self.first.value
#             self.first = self.first.next
#             if(self.first != None):
#                 self.first.prev = None

#             if(self.first == None):
#                 self.last = None
#         else:
#             return False
#         return value
    

#     def head(self):
#         if(self.first != None):
#             return self.first.value

#     def tail(self):
#         return self.last.value

#     def empty(self):
#         return True if self.first == None else False

#     def print(self):
#         lst = []
#         last = self.first
#         while (last != None):
#             # print(last.value,end=", ")
#             lst.append(last.value)
#             last = last.next
#         return lst

        
# me = Queue()
# meP = Queue()
# you = Queue()
# youP = Queue()

# act = {
#     0 : "Eat",
#     1 : "Game",
#     2 : "Learn",
#     3 : "Movie"
# }
# place = {
#     0 : "Res.",
#     1 : "ClassR.",
#     2 : "SuperM.",
#     3 : "Home"
# }

# x = input("Enter Input : ").split(',')
# score = 0
# for i in x:
#     m,y = i.split()
#     me.insert(m)
#     you.insert(y)
    
#     mA,mP = m.split(':')
#     yA,yP = y.split(':')
#     meP.insert(act[int(mA)]+":"+place[int(mP)])
#     youP.insert(act[int(yA)]+":"+place[int(yP)])
  

#     logic = [1 if mA == yA else 0 ,2 if mP == yP else 0]
    
#     sc = 1 << sum(logic)
#     sc = sc >> 1
    
#     score += sc if sc != 0 else -5 

# print("My   Queue = ",end="")
# print(*me.print(),sep=", ")
# print("Your Queue = ",end="")
# print(*you.print(),sep=", ")
# print("My   Activity:Location = ",end="")
# print(*meP.print(),sep=", ")
# print("Your Activity:Location = ",end="")
# print(*youP.print(),sep=", ")

# if(score > 6):
#     print("Yes! You're my love! : Score is ",end="")
# elif(score >= 0):
#     print("Umm.. It's complicated relationship! : Score is ",end="")
# else:
#     print("No! We're just friends. : Score is ",end="")
# print(score,".",sep="")


# # TENET
# class DeQueue:
    
#     class Node:

#         def __init__(self,value):
#             self.value = value
#             self.next = None
#             self.prev = None

#     def __init__(self):
#         self.last = None
#         self.first = None
        

#     def push_back(self,value):
#         newNode = self.Node(value)
#         if(self.first == None):
#             self.first = newNode
#             self.last = newNode
#         else : 
#             self.last.next = newNode
#             newNode.prev = self.last
#             self.last = newNode
    

#     def push_front(self,value):
#         newNode = self.Node(value)
#         if(self.first == None):
#             self.first = newNode
#             self.last = newNode
#         else : 
#             self.first.prev = newNode
#             newNode.next = self.first
#             self.first = newNode
          

#     def pop_front(self):
#         if(self.first != None):
#             value = self.first.value
#             self.first = self.first.next
#             if(self.first != None):
#                 self.first.prev = None

#             if(self.first == None):
#                 self.last = None
#         else:
#             return False
#         return value
    
#     def pop_back(self):
#         if(self.last != None):
#             value = self.last.value
#             self.last = self.last.prev
             
#             if(self.last == None):
#                 self.first = None
#             else:
#                 self.last.next = None
#         else:
#             return False
#         return value
    

#     def head(self):
#         if(self.first != None):
#             return self.first.value

#     def tail(self):
#         return self.last.value

#     def empty(self):
#         return True if self.first == None else False

#     def print_queue(self):
#         lst = []
#         last = self.first
#         while (last != None):
#             # print(last.value,end=", ")
#             lst.append(last.value)
#             last = last.next
#         return lst
    
    
#     def print_stack(self):
#         lst = []
#         last = self.last
#         while (last != None):
#             # print(last.value,end=", ")
#             lst.append(last.value)
#             last = last.prev
#         return lst


# r,b = input("Enter Input (Red, Blue) : ").split()

# red = DeQueue()
# blue = DeQueue()
# blue_left = DeQueue()

# explo = [0,0]

# mistake = 0

# for i in b:
    
#     if(blue_left.empty()):
#         blue_left.push_back([i,1])
#     else :
#         tail = blue_left.tail()
#         if(tail[0] == i):
#             if(tail[1] + 1 == 3):
#                 explo[1] += 1
#                 blue.push_back(i)
#                 blue_left.pop_back()
#                 blue_left.pop_back() 
#             else:
#                 blue_left.push_back([i,2])
#         else:
#             blue_left.push_back([i,1])

 
# for i in r:
#     if(red.empty()):
#        red.push_front([i,1])
#     else:
#         tail = red.tail()
#         if(tail[0] == i):
#             if(tail[1] == 2):
#                 bb = blue.pop_back() # blue bomb
#                 if(bb):
#                     if(bb == tail[0]): # bb is same as rb
#                         mistake += 1
#                         red.pop_back()
#                         red.pop_back()
#                         red.push_back([i,1]) 
#                     else:   # bb blocked rb
#                         red.push_back([bb,1])
#                         red.push_back([i,1])
#                     continue
#                 else:
#                     explo[0] += 1
#                     red.pop_back()
#                     red.pop_back()
#                     continue
                    
#             red.push_back([i,2])
#         else:
#             red.push_back([i,1])

# redLst = red.print_stack()
# print("Red Team :")
# print(len(redLst))
# if(len(redLst) > 0):
#     print(*[i[0] for i in redLst],sep="")
# else:
#     print("Empty")
# print(explo[0],"Explosive(s) ! ! ! (HEAT)")
# if(mistake):
#     print("Blue Team Made (a) Mistake(s)",mistake,"Bomb(s)")
# print("----------TENETTENET----------")
# print(": maeT eulB")
# blueLst = blue_left.print_queue()
# print(len(blueLst))
# if(len(blueLst) > 0):
#     print(*[i[0] for i in blueLst],sep="")
# else:
#     print("ytpmE")
# print("(EZEERF) ! ! ! (s)evisolpxE",explo[1])