# # find max

# def findMax(lst,index,max):
#     if(len(lst) - 1 < index):
#         return max
    
#     if( max == None or max < int(lst[index]) ):
#         max = int(lst[index])
    
    
#     return findMax(lst,index+1,max)
    
# lst = input("Enter Input : ").split()

# print("Max :",findMax(lst,0,None))

# # find length
# def itrerate(lst,index,co):
    
#     try:
#         lst[index]
#     except:
#         return co

#     print(lst[index],end="")
#     if(index % 2 == 0):
#         print("*",end="")
#     else:
#         print("~",end="")
    
#     return itrerate(lst,index+1,co+1)

# def length(txt):    
#     l = itrerate(txt,0,0) 
#     print("\n{0}".format(l))


# length(input("Enter Input : "))


# # digital on your area
# def findLength(num,div):
    
#     if( 1 << div >= num):
#         return  div
#     else:
#         return findLength(num,div+1)

# def getDecimal(num,res):
    
#     if(num==0):
#         return res
#     res = str( (num) & 1) + res

#     return getDecimal(num >> 1,res)



# def decimal(num,l,max):
#     if(num > max):
#         return 
#     dec = getDecimal(num,"")
#     print( (l - len(dec)) * "0",dec,sep="" )
#     decimal(num+1,l,max)


# x = input("Enter Number : ")
# x = int(x)
# if(x<0):
#     print("Only Positive & Zero Number ! ! !")
#     exit()
# else:
#     l = findLength(2**x -1,1)
#     l = int(l)
#     decimal(0,l,2**x -1)

# # perket
# def findLength(num,div):
    
#     if( 1 << div >= num):
#         return  div
#     else:
#         return findLength(num,div+1)

# def getDecimal(num,res):
    
#     if(num==0):
#         return res
#     res = str( (num) & 1) + res

#     return getDecimal(num >> 1,res)


# lst = []
# def decimal(num,l,max,ans = None):
    
#     if(num > max):
#         return ans
#     dec = getDecimal(num,"")
#     tryAll =  ((l - len(dec)) * "0") +dec 
#     s = 1
#     b = 0
#     for i in range(0,len(tryAll)):
#         if(tryAll[i] == "1"):
#            s *= int(lst[i].split()[0])
#            b += int(lst[i].split()[1])

#     if(ans == None):
#         ans = abs(s-b)
#     else:
#         ans = ans if abs(s-b) > ans else abs(s-b)

#     return decimal(num+1,l,max,ans)

# lst = input("Enter Input : ").split(',')
# x = len(lst)
# l = findLength(2**x-1,1)
# l = int(l)
# ans = decimal(1,l,2**x-1,None)
# print(ans)

# asteroid
def goForth(asts,index):

    if(len(asts)-1 <index or index < 0):
        return None
    
    if(asts[index] == 0):
        return goForth(asts,index +1 )
    else:
        return index

def goBackward(asts,index):
    if(len(asts)-1 < index or index < 0):
        return None
    
    if(asts[index] == 0):
        return goBackward(asts,index - 1)
    else:
        return index

def asteroid_collision(asts,index):

    if(len(asts)-1 <index or index < 0):
        return

    if(asts[index] == 0):
        index += 1
    else:
        value = asts[index]
        dir = "left" if value < 0 else "right"
        next = goForth(asts,index + 1) if value > 0 else goBackward(asts,index - 1)
        if(next == None):
            index += 1
            pass
        else:
            nextValue = asts[next]
            if(dir == "left"): # value is  negative
                if(nextValue > 0):
                    if(abs(nextValue) > abs(value)):
                        asts[index] = 0
                    elif(abs(nextValue) == abs(value)):
                        asts[next] = 0
                        asts[index] = 0
                    index = next 
                else:
                    index += 1
            else:           # value is postitive
                if(nextValue < 0):
                    if(abs(nextValue) > abs(value)):
                            asts[index] = 0
                    elif(abs(nextValue) == abs(value)):
                        asts[next] = 0
                        asts[index] = 0
                    index = next
                else:
                    index += 1
            
    return asteroid_collision(asts,index)

def deleteZero(lst,index=0,res = []):

    if(len(lst) -1 < index):
        return res
    if(lst[index] == 0):
        pass
    else:
        res.append(lst[index])

    return deleteZero(lst,index+1,res)
    

x = input("Enter Input : ").split(",")
x = list(map(int,x))

asteroid_collision(x,0)
print(deleteZero(x))

