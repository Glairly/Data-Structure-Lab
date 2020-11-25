# 1
# lst = input("Enter : ").split(",")

# group = []
# graph = {}

# for i in lst:
#     x,y = i.split()
#     if(x not in group):
#        group.append(x)
#        graph[x] = []
#     if(y not in group):
#        group.append(y)
#        graph[y] = []
    
#     graph[x].append(y)
 
# group = sorted(group)
  
# print("    " + "  ".join(group))
# for i in group:
#     lst = ['0' for i in range(len(group))]
#     for j in graph[i]:
#         lst[group.index(j)] = '1'
#     print(i,":",", ".join(lst))



# #2
# lst = input("Enter : ").split(",")

# group = []
# graph = {}

# for i in lst:
#     x,y = i.split()
#     if(x not in group):
#        group.append(x)
#        graph[x] = []
#     if(y not in group):
#        group.append(y)
#        graph[y] = []
    
#     graph[x].append(y)
#     graph[y].append(x)

 
# group = sorted(group)

# def dfs(lst,graph):
#     visited = []
#     ans = []
#     while(len(visited) < len(lst)):
#         q = []
#         for i in lst:
#             if i not in visited:
#                 q = [i]
#                 break
     
#         while(len(q)):
#             x = q.pop(0)
#             if(x in visited):
#                 continue
#             ans.append(x)
#             visited.append(x)
#             for j in  sorted(graph[x]):
#                 q.append(j)

#         # for j in (graph[x]):
#         #     q.append(j)
#     return ans

# def bfs(lst,graph):
#     visited = []
#     ans = []
#     while(len(visited) < len(lst)):
#         st = []
#         for i in lst:
#             if i not in visited:
#                 st = [i]
#                 break
#         while(len(st)):
#             x = st.pop()
#             if(x in visited):
#                 continue
#             ans.append(x)
#             visited.append(x)
#             for j in sorted(graph[x],reverse=True):
#                     st.append(j)
#     return ans

# print("Depth First Traversals :",*bfs(group,graph))
# print("Bredth First Traversals :",*dfs(group,graph))
 

# 3
# lst,travel = input("Enter : ").split("/")

# lst = lst.split(",")
# travel = travel.split(",")

# group = []
# graph = {}

# for i in lst:
#     x,w,y = i.split()
#     w = int(w)
#     if(x not in group):
#        group.append(x)
#        graph[x] = []
#     if(y not in group):
#        group.append(y)
#        graph[y] = []
    
#     graph[x].append([y,w])
    

 
# group = sorted(group)

# class PriorityQueue:

#     def __init__(self,operator = lambda x,y : x < y ):
#         self.list = []
#         self.operator =  operator

#     def insert(self,value):
#         i = 0
#         while( i < len(self.list) and self.operator(value,self.list[i])):
#             i += 1
#         self.list.insert(i,value)
    
#     def pop(self):
#         return self.list.pop(0)
    
#     def __str__(self):
#         s = ""
#         for i in self.list:
#             s += str(i) + " "
#         return s
    
#     def __len__(self):
#         return len(self.list)

# def dijkstra(lst,graph,src,des):
#     visited = {}
#     ans = PriorityQueue(lambda x,y: len(x[0]) >=  len(y[0]) or x[1] >=  y[1] )
#     for i in lst:
#         visited[i] = -1
#     pq = PriorityQueue(lambda x,y: x[1] >= y[1])
#     pq.insert([src,0,[src]])

#     while(len(pq)):
#         x,w,l = pq.pop()
         
#         if(visited[x] != -1 and  w > visited[x]):
#             continue
        
#         visited[x] = w
#         if x == des:
#            ans.insert([l,w])
#            continue
#         if(visited[des] != -1 and w >= visited[des]):
#             continue
#         for j in graph[x]:
#             pq.insert( [ j[0] , j[1] + w , l + [j[0]]] )
#         # for j in (graph[x]):
#         #     q.append(j)
#     return ans



# for i in graph.keys():
#     graph[i] = sorted(graph[i])


# for i in travel:
#     x,y = i.split()
#     if(x not in group or y not in group):
#       print("Not have path :",x,"to",y)  
#       continue
#     lst = dijkstra(group,graph,x,y)
#     if not lst :
#         print("Not have path :",x,"to",y)
#     else:
#         # print(lst)
#         print(x,"to",y,":","->".join(lst.list[0][0]))



 

# #5
# lst,travel = input("Enter Input : ").split("/")

# lst = lst.split(",")
# src,des = travel.split()

# group = []
# graph = {}

# for i in lst:
#     x,y = i.split()
#     if(x not in group):
#        group.append(x)
#        graph[x] = []
#     if(y not in group):
#        group.append(y)
#        graph[y] = []
    
#     graph[x].append(y)
#     graph[y].append(x)


# visited = []
# ans = []
# maxlen = 0
# def solve(lst,x):
#     global graph,group,des,visited,ans,maxlen
#     if(x in visited):
#         return
#     if(x == des):
#         ans.append(lst)
#         if(maxlen < len(lst)):
#             maxlen = len(lst)
#         return
#     visited.append(x)
#     for j in  sorted(graph[x]):
#         solve(lst+[j],j)
#     visited.remove(x)

# solve([src],src)


# if(not len(ans)):
#     print(src,"can't go to",des)
#     exit()
# print("All possible path from {0} to {1} :".format(src,des))
# for i in range(1,maxlen + 1):
#     lst = list(filter(lambda x: len(x) == i,ans))
#     for j in lst:
#         print(" -> ".join(j))
