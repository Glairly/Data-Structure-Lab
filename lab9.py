def swap(a,b):
    a,b = b,a
# def bubblesort(list,index):

#     if(index + 1 >= len(list)):
#         if(list[index-1] > list[index]):
#             return True
#         return False
    
#     if(list[index] > list[index+1]):
#         swap(list[index],list[index+1])
     
    
#     bol = bubblesort(list,index+1)
#     if(index != 0 and list[index-1] > list[index]):
#         return True
#     return bol
 

# def sorting(list):
#     while bubblesort(list,0):
#         pass
#     return list



# inp = input("Enter Input : ").split()
# inp = [int(i) for i in inp]

# lst = sorting(inp) 
# print (lst)



# def mergesort(list,left,right):
#     if(left < right):
#         mid = (left + right)//2
#         mergesort(list,left,mid)
#         mergesort(list,mid+1,right)
#         merge(list,left,mid+1,right) 

# def merge(list,left,mid,right):
#     l = left
#     r = mid
#     newList = []
#     while(l <= mid - 1 and r <= right ):
#         data = ""
#         if(list[l] < list[r]):
#             data = list[l]
#             l += 1
#         else:
#             data = list[r]
#             r += 1
#         newList.append(data)
    
#     while(l <= mid-1):
#         newList.append(list[l])
#         l+=1
#     while(r <= right):
#         newList.append(list[r])
#         r+=1
    
#     co = 0
#     for i in range(left,right + 1):
#         list[i] = newList[co]
#         co += 1

# Unsigned Sort
# lst = input("Enter Input : ").split()
# lst = [int(i) for i in lst]
# lst2  = []
# dic =  {}

# for i in range(len(lst)):
#     if(lst[i] < 0):
#         dic[i] = lst[i]
#     else:
#         lst2.append(lst[i])

# mergesort(lst2,0,len(lst2)-1)


# for i in dic.keys():
#     lst2.insert(i,dic[i])

# print (*lst2)

# def mergesort(list,left,right,reverse = False):
#     if(left < right):
#         mid = (left + right)//2
#         mergesort(list,left,mid,reverse)
#         mergesort(list,mid+1,right,reverse)
#         merge(list,left,mid+1,right,reverse) 


# def merge(list,left,mid,right,reverse):
#     l = left
#     r = mid
#     newList = []
#     while(l <= mid - 1 and r <= right ):
#         data = ""
#         if(list[l] < list[r] if not reverse else list[l] > list[r]):
#             data = list[l]
#             l += 1
#         else:
#             data = list[r]
#             r += 1
#         newList.append(data)
    
#     while(l <= mid-1):
#         newList.append(list[l])
#         l+=1
#     while(r <= right):
#         newList.append(list[r])
#         r+=1
    
#     co = 0
#     for i in range(left,right + 1):
#         list[i] = newList[co]
#         co += 1


# somethindDrome 
# inp = int(input("Enter Input : "))
# dic = {}
# dup = False
# lst = []
# while(inp > 0):
#     t =  inp % 10 
#     if(t not in dic.keys()):
#         dic[t] = 1
#     else:
#         dup = True
#     lst.append(int(t))
#     inp //= 10


# MetaList = [int(i) for i in lst]
# KetaList = [int(i) for i in lst]

# mergesort(MetaList,0,len(MetaList)-1,reverse= True)
# mergesort(KetaList,0,len(KetaList)-1)

# if(len(dic.keys()) == 1):
#     print("Repdrome")
#     exit()

# if(not dup):
#     if(MetaList == lst):
#         print("Metadrome")
#         exit()
#     if(KetaList == lst):
#         print("Katadrome")
#         exit()
# else:
#     if(MetaList == lst):
#         print("Plaindrome")
#         exit()
#     if(KetaList == lst):
#         print("Nialpdrome")
#         exit()

# print("Nondrome")


# def insertionSort(list,sorted,index):
#     if(index >= len(list)):
#         if(list[index-2] > list[index-1]):
#             return True
#         else:
#             return False

#     i = 0
#     while(i < len(sorted) and sorted[i] < list[index]):
#         i += 1
#     sorted.insert(i,list[index])
#     bal = insertionSort(list,sorted,index+1)
#     if(index != 0 and list[index-1] > list[index]):
#          return True
#     else:
#          return bal


# def sorting(list):
#     lst = []
#     while insertionSort(list,lst,0):
#           list = lst;
#           lst =  [];
#     return lst

# def getMedian(list):
#     leg = len(list) - 1
#     if(leg % 2 == 1):
#         return (list[leg//2] + list[leg//2 + 1])/2
#     else:
#         return list[leg//2]

# l = [e for e in input("Enter Input : ").split()]
# if l[0] == 'EX':
#     Ans = "minHeap and maxHeap"
#     print("Extra Question : What is a suitable sort algorithm?")
#     print("   Your Answer : "+Ans)
# else:
#     l = list(map(int, l))
#     lst = []
#     for i in l:
#         lst.append(i)
#         print("list =",lst,": median = %.1f" % getMedian(sorting(lst)))



def mergesort(list,left,right,reverse = False):
    if(left < right):
        mid = (left + right)//2
        mergesort(list,left,mid,reverse)
        mergesort(list,mid+1,right,reverse)
        merge(list,left,mid+1,right,reverse) 


def merge(list,left,mid,right,reverse):
    l = left
    r = mid
    newList = []
    while(l <= mid - 1 and r <= right ):
        data = ""
        if(list[l][1]['points'] < list[r][1]['points'] if not reverse else list[l][1]['points'] > list[r][1]['points']):
            data = list[l]
            l += 1
        elif(list[l][1]['points'] > list[r][1]['points'] if not reverse else list[l][1]['points'] < list[r][1]['points']):
            data = list[r]
            r += 1
        else:
            if list[l][2]['gd'] < list[r][2]['gd'] if not reverse else list[l][2]['gd'] > list[r][2]['gd'] :
                data = list[l]
                l+=1
            else:
                data = list[r]
                r+=1

        newList.append(data)
    
    while(l <= mid-1):
        newList.append(list[l])
        l+=1
    while(r <= right):
        newList.append(list[r])
        r+=1
    
    co = 0
    for i in range(left,right + 1):
        list[i] = newList[co]
        co += 1


inp = input("Enter Input : ").split("/")
lst = []
for i in inp:
    
    raw = i.split(",")
    lst.append([
        raw[0],
        {'points' : 3 * int(raw[1]) + int(raw[3])},
        {'gd' :  int(raw[4]) - int(raw[5])}
    ])

mergesort(lst,0,len(lst)-1,reverse=True)
print("== results ==")
print(*lst,sep="\n")