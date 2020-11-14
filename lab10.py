# #1
# def bi_search(l, r, arr, x):
#     # Code Here
#     if(l == r):
#         return arr[r] == x
    
#     mid = (l + r)//2 + 1
#     if(arr[mid] > x):
#         return bi_search(l,mid-1,arr,x)
#     else:
#         return bi_search(mid,r,arr,x)

# inp = input('Enter Input : ').split('/')
# arr, k = list(map(int, inp[0].split())), int(inp[1])
# print(bi_search(0, len(arr) - 1, sorted(arr), k))

# #2
# def bi_search(l, r, arr, x):
#     if(l == r):
#         if arr[l] > x :
#             return arr[l]
#         else: 
#             return None

#     mid = (l + r)//2 + 1
#     res = None
#     if(arr[mid] > x):
#         res = bi_search(l,mid-1,arr,x)
#     else:
#         res = bi_search(mid,r,arr,x)
#     return res if res else (arr[mid] if arr[mid] > x else None)


# inp = input('Enter Input : ').split('/')
# arr, arr2 = sorted(list(map(int, inp[0].split()))), list(map(int, inp[1].split()))
# for k in arr2:
#     res =  bi_search(0, len(arr) - 1, arr, k) 
#     print(res if res else "No First Greater Value")

#3
# class Data:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

#     def __str__(self):
#         return "({0}, {1})".format(self.key, self.value)

# class hash:

#     def __init__(self,max,chain):
#         self.data = [None for i in range(max)]
#         self.limit= max
#         self.chain= chain
#         self.length = 0

#     def code(self,a):
#         return sum([ord(i) for i in a])  

#     def isFull(self):
#         return self.length == self.limit

#     def insert(self,value):
#         key,val = value.split(" ")
#         s = self.code(key)
#         co = 0
#         now = 0
#         while(co <= self.chain):
#             if(co != 0):
#                 print ("collision number",co,"at",now)
#                 if(co == self.chain):
#                     break
#             now = (s + (0 if not co else  co*co) ) % self.limit 
             

#             if(self.data[now] == None):
#                 self.data[now] = Data(key,val)
#                 self.length += 1
#                 break
#             co += 1

#         if(co >= self.chain):
#             print("Max of collisionChain")


#     def __str__(self):
#         return  "\n".join(list(map(str,[ "#{0}	{1}".format(str(i+1),self.data[i]) for i in range( len(self.data) ) ] ) ) )  + "\n---------------------------"


# print(" ***** Fun with hashing *****")

# val,arr = input("Enter Input : ").split("/")

# h = hash(int(val.split(" ")[0]),int(val.split(" ")[1]))

# arr = arr.split(",")

# for i in arr:
#     h.insert(i)
#     print(h)
#     if(h.isFull()):
#         print("This table is full !!!!!!")
#         break


#4
# import math
# class Data:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)

# class hash:

#     def __init__(self,max,chain,t):
#         self.data   = [None for i in range(max)]
#         self.limit  = max
#         self.chain  = chain
#         self.length = 0
#         self.threshold = t
#         self.bu = list()

#     def code(self,a):
#         # return sum([ord(i) for i in a])  
#         return int(a)

#     def isFull(self):
#         return self.length == self.limit

#     def findNearPrime(self):
#         i = self.limit * 2
#         while(True):
#             c = True
#             for j in range(2, int(math.sqrt(i)) + 1):
#                 if(not i % j):
#                     i += 1
#                     c = False
#                     break
#             if c :
#                 break

#         return i

#     def handlerIllegal(self,co,value):
#         if(self.length * 100 // self.limit >= self.threshold):
#             print("****** Data over threshold - Rehash !!! ******")
#             self.resize()
#             self.Rehash()
#         elif (co >= self.chain):
#             print("****** Max collision - Rehash !!! ******")
#             self.resize()
#             self.Rehash()

#     def resize(self):
#         self.data += [None for i in range(self.findNearPrime() - self.limit)]
#         self.limit = len(self.data)

#     def Rehash(self):
#         for i in range(self.limit):
#             self.data[i] = None
#         for i in self.bu:
#             self.insert(i,False)

#     def insert(self,value,Rehash = True):
#         s = self.code(value)
#         co = 0
#         now = 0
#         while(co <= self.chain):
#             if(co != 0):
#                 print ("collision number",co,"at",now)
#                 if(co == self.chain):
#                     break
#             now = (s + (0 if not co else  co*co) ) % self.limit 

#             if(self.data[now] == None):
#                 self.data[now] = Data(value)
#                 if(Rehash):
#                     self.length += 1
#                 break
#             co += 1

#         if(Rehash):
#             self.handlerIllegal(co,value)

#     def addBuff(self,value):
#         self.bu.append(value)

#     def __str__(self):
#         return  "\n".join(list(map(str,[ "#{0}	{1}".format(str(i+1),self.data[i]) for i in range( len(self.data) ) ] ) ) )  + "\n----------------------------------------"


# print(" ***** Rehashing *****")

# val,arr = input("Enter Input : ").split("/")

# h = hash(int(val.split(" ")[0]),int(val.split(" ")[1]),int(val.split(" ")[2]))

# arr = arr.split()

# print("Initial Table :",h,sep="\n")

# for i in arr:
#     print("Add :",i)
#     h.addBuff(i)
#     h.insert(i)
#     print(h)
#     if(h.isFull()):
#         print("This table is full !!!!!!")
#         break


# 5
boxes = 0
ans   = -1
def solve(dpArr,list,box,i):
    global boxes 
    global ans
    if(box == boxes):
        s = 0
        for j in list:
            s += len(j)
        
        if(s == len(dpArr)):
            mx = 0
            for j in list:
                if(sum(j) > mx):
                    mx = sum(j)

            if(mx < ans or ans == -1):
                ans = mx                
        return

    for j in range(1,len(dpArr) + 1):
        if ( i + j > len(dpArr)  ):
            break
        solve(dpArr,list + [dpArr[i:i + j]],box + 1 ,i + j)


inp = input("Enter Input : ")

inp,boxes = list(map(int,inp.split("/")[0].split() )) , int( inp.split("/")[1])

# for i in range(1,len(inp)):
#     inp[i] += inp[i-1]

solve(dpArr = inp,list = [],box = 0,i = 0)
print("Minimum weigth for",boxes,"box(es) =",ans)