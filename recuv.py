# stack = [[5,4,3,2,1],[],[]]

# def move(n,src,aux,des):

#     if(n == 1):
#         print(n,'from',src,'to',aux)
#         stack[aux].append(stack[src].pop())
#         print(stack)
#     else :
#         move(n-1,src,des,aux)
#         print(n,'from',src,'to',aux)
#         stack[aux].append(stack[src].pop())
#         print(stack)
#         move(n-1,des,aux,src)



# move(5,0,2,1)

# def knapsack(select:list,list,sum,limit):
#     co = 0
#     if(len(list) <= 0):
#         return 0
#     if(sum+list[0] > limit):
#         return 0
#     elif(sum+list[0] == limit):
#         print([select ,list[0]])
#         return 1
#     else:
#        select.append(list[0])
#        co +=  knapsack(select ,list[1:],sum+list[0],limit)
#     select.pop()
#     co += knapsack(select,list[1:],sum,limit)
#     return co 

# t = knapsack([],[1,2,4,5,2,10,2],0,14)
# print (t)


def toBit(n):
    if n == 0:
        return ''
    else:
        return toBit(n >> 1) + str(n & 1)

def bitLength(num,n):
    if num == 0:
        return n
    else:
        return bitLength(num >> 1,n + 1)

val = 5
msb = 2**val - 1
length = bitLength(msb,0)
for i in range(msb + 1):
    bits = toBit(i)
    bits = '0'*(length - len(bits)) + bits
    print(bits)