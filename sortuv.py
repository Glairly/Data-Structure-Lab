# # def swap(a,b):
# #     a,b = b,a

# # def quicksort(lst,low = 0,hi = -5555):
# #     if(hi == -5555):
# #         hi = len(lst) - 1
# #     if hi <= low:
# #         return lst
# #     i = low + 1 
# #     j = hi 
# #     div = low 
# #     while True:
# #         while  i <= j and  (lst[i] == lst[div]) : # skip same number
# #             i += 1
# #         while  j >= i and  (lst[j] == lst[div]) : # skip same number
# #             j -= 1
        
       
# #         if(j < i):  # meet at mid 
# #             lst[j],lst[div] = lst[div],lst[j]
# #             div = j
# #             break
# #         elif lst[j] < lst[div]: # 
# #             lst[j],lst[i] = lst[i],lst[j]
# #             i += 1
# #         elif lst[i] > lst[div]:
# #             lst[j],lst[i] = lst[i],lst[j]
# #             j -= 1
# #         else:
# #             i += 1
    
# #     quicksort(lst,low,div-1)
# #     quicksort(lst,div+1,hi)



# # lst = [9,3,4,8,1,2]
# # quicksort(lst)
# # print (lst)


# def quicksort(lst,low,hi):
#     if(hi <= low):
#         return
#     i = low + 1
#     j = hi 
#     div = low
#     while(True):

#         while i <= j and (lst[i] == div):
#             i += 1
#         while j >= i and (lst[j] == div):
#             j += 1
        
#         if(j < i):
#             lst[j],lst[div] = lst[div],lst[j]
#             div = j
#             break
#         elif lst[j] < lst[div]:
#             lst[j],lst[i] = lst[i],lst[j]
#             i += 1
#         elif lst[i] > lst[div]:
#             lst[j],lst[i] = lst[i],lst[j]
#             j -= 1
#         else:
#             i += 1
    
#     quicksort(lst,low,div-1)
#     quicksort(lst,div+1,hi)


# lst = [9,3,4,8,1,2]

# quicksort(lst,0,5)

# print(lst)



# # def mergeSort(lst,l,r):
# #     if(r <= l ):
# #         return
# #     mid = (l + r) // 2
# #     mergeSort(lst,l,mid)
# #     mergeSort(lst,mid+1,r)
# #     merge(lst,l,mid+1,r)


# # def merge(lst,left,mid,right):
# #     l = left
# #     r = mid 
# #     newList = []
# #     while(l <= mid and r <= right):
# #         data = None
# #         if (lst[l] < lst[r]):
# #             data = lst[l]
# #             l += 1
# #         else:
# #             data = lst[r]
# #             r += 1
# #         newList.append(data)

# #     while(l <= mid):
# #         newList.append(lst[l])
# #         l+= 1
# #     while(r <= right):
# #         newList.append(lst[r])
# #         r += 1
    
# #     for i in range(left,right + 1):
# #         lst[i] = newList[i - left]



# # lst = [9,3,4,8,1,2]
# # mergeSort(lst,0,5)
# # print (lst)
 
def mergeSort(lst,left,right):
    if(right > left):
        mid = (left + right)//2
        mergeSort(lst,left,mid)
        mergeSort(lst,mid+1,right)
        merge(lst,left,mid+1,right)

def merge(lst,left,mid,right):
    l = left
    r = mid
    newList = []
    while(l < mid and r <= right):
        data =  None
        if(lst[l] < lst[r]):
            data = lst[l]
            l += 1
        else:
            data = lst[r]
            r += 1
        newList.append(data)
    
    while(l < mid):
        newList.append(lst[l])
        l += 1
    while(r <= right):
        newList.append(lst[r])
        r += 1

    for i in range(left,right+1):
        lst[i] = newList[i - left]
    
from numpy import random
size =  10000
x = random.randint(100000,size = size)

print(x)
mergeSort(x,0,size - 1)
print(list(x))