###### วงเล็บโง่ๆ #######
#x = input("Enter Input : ")
#
#x = list(x)
#lst = []
#lst_1 = []
#lst2 = []
#lst_2 = []
#
#for i in x:
    
#    if(i == '('):
#        lst.append(i)
#    if(i == '[' ):
#        lst2.append(i)
#    if(i == ')'):
#        lst_1.append(i)
#    if(i == ']' ):
#        lst_2.append(i)
    
#need = abs( len(lst) - len(lst_1) ) + abs(len(lst2) - len(lst_2))
#print(need)
#if (need ==  0):
#    print("Perfect ! ! !")

####### จานโง่ๆ #######
# x = input("Enter Input : ").split(',')

# lst = [] 

# for i in x:
#     w,hz = i.split()
#     if(len(lst) == 0):
#         lst.append(i)
#     else : 
#         last = lst[-1:][0]
#         nw,nhz = last.split()
#         while(int(w) > int(nw)):
#            print(nhz)
#            lst.pop()
#            if(len(lst) > 0):
#                 last = lst[-1:][0]
#                 nw,nhz = last.split() 
#            else:
#                 break
#         lst.append(i)

####### Combo โง่ๆ #######
# x = input("Enter Input : ").split()


# lst = [] 
# combo = 0
# for i in x:
#     if(len(lst) == 0):
#         lst.append([i,1])
#     elif (lst[-1:][0][0] == i) :
#         co = 0
#         if(lst[-1:][0][1] + 1 == 3):
#             combo += 1
#             for ii in range(2):
#                 lst.pop()
#         else:
#             lst.append([i,2])
#     else :
#         lst.append([i,1])
        
# print(len(lst))
# if(len(lst) > 0):
#     while(len(lst) > 0):
#         print(lst[-1:][0][0],end="")
#         lst.pop()
#     if(combo > 1):
#         print("\nCombo :",combo,"! ! !")
# else: 
#     print("Empty")
#     if(combo > 1):
#             print("Combo :",combo,"! ! !")

# A C C A A A C A A

####### เครื่องคิดเลข โง่ๆ #######
# class StackCalc:

#     def __init__(self):
#         self.lst = []
#         self.valid = ["DUP","+","-","/","*","POP","PSH"]
#         self.order = ["+","-","/","*"]
#         self.operand = [lambda x: x[0] + x[1],lambda x: x[0] - x[1],lambda x: x[0] / x[1],lambda x: x[0] * x[1]]
#         self.value = 0
#         self.Invalid = False

#     def run(self,arg):
#         self.value = 0
#         for i in arg.split():
#             if ( not self.isNumber(i) and i not in self.valid):
#                 print("Invalid instruction:",i)
#                 self.Invalid = True
#                 break
#             else:
#                 if(self.isNumber(i)):
#                     self.lst.append(i)
#                 else:
#                     if(i == "DUP"):
#                         t = self.lst[-1:][0]
#                         self.lst.append(t)
#                     elif(i == "POP"):
#                         self.lst.pop()
#                     elif(i == "PSH"):
#                         pass
#                     else:
#                         if(len(self.lst) > 1):
#                             l = [int(self.lst.pop()),int(self.lst.pop())]
#                             self.lst.append(int(self.operand[self.order.index(i)](l)))
                    
                    
              
####### SOI full โง่ๆ #######
#     def getValue(self):
#         if(not self.Invalid):
#             return  self.lst[-1:][0] if len(self.lst) > 0  else 0
#         else:
#             return ''
    
#     def isNumber(self,x):
#         try:
#             int(x)
#             return True
#         except ValueError:
#             return False

# print("* Stack Calculator *")
# arg = input("Enter arguments : ")
# machine = StackCalc()
# machine.run(arg)
# print(machine.getValue())
 
# print("******** Parking Lot ********")
# x = input("Enter max of car,car in soi,operation : ").split() # [max,stack car,command,number of car]

# lst = []
# for i in x[1].split(','):
#     if(i == '0'):
#         break
#     lst.append(i)

# if (x[2] == "arrive"):
#     if(len(lst) + 1 > int(x[0])):
#         print("car",x[3],"cannot arrive : Soi Full")
#     elif(x[3] not in lst):
#         lst.append(x[3])
#         print("car",x[3],"arrive! : Add Car",x[3])
#     else:
#         print("car",x[3],"already in soi")
# else:
#     if(len(lst) == 0):
#         print("car",x[3],"cannot depart : Soi Empty")
#     elif(x[3] in lst):
#         print("car",x[3],"depart ! : Car",x[3],"was remove")
#         lst.remove(x[3])
#     else:
#         print("car",x[3],"cannot depart : Dont Have Car",x[3])
    
# lst = [int(i) for i in lst]
# print(lst)

 

 