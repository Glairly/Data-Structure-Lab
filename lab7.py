# # bst & min,max & lessEqual
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def __str__(self):
#         return str(self.data)

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         newNode = Node(data)
#         if(self.root == None):
#             self.root = newNode
#             return self.root


#         ptr = self.root
#         while(True):
#             if(data < ptr.data): # go left
#                 if(ptr.left == None):
#                     ptr.left = newNode
#                     return self.root
#                 else:
#                     ptr = ptr.left
#             if(data >= ptr.data): # go right
#                 if(ptr.right == None):
#                     ptr.right = newNode
#                     return self.root
#                 else:
#                     ptr = ptr.right
    
#     def printTree(self, node, level = 0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)

#     def min(self,root):
#         ptr = root
#         if(ptr == None):
#             return None
#         while(ptr.left != None):
#             ptr = ptr.left
#         return ptr.data
    
#     def max(self,root):
#         ptr = root
#         if(ptr == None):
#             return None
#         while(ptr.right != None):
#             ptr = ptr.right
#         return ptr.data
    
#     def lessEqual(self,node,value):
#         if(node == None):
#             return 0
#         co = 0
#         co += self.lessEqual(node.left,value)
#         co += self.lessEqual(node.right,value)
#         if(node.data <= value):
#             co += 1
#         return co

# T = BST()

# # inp = [int(i) for i in input('Enter Input : ').split()]

# # lessEqual
# inp = [i for i in input('Enter Input : ').split()]
# inp[-1],k = inp[-1].split('/')
# inp = [int(i) for i in inp]
# k = int(k)

# for i in inp:
#     root = T.insert(i)
# T.printTree(root)

# print("--------------------------------------------------")
# # min,max
# # print("Min :", T.min(root) )
# # print("Max :", T.max(root) )

# # lessEqual
# print(T.lessEqual(root,k))



# # pre, in, postoder and breadth
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def __str__(self):
#         return str(self.data)

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         newNode = Node(data)
#         if(self.root == None):
#             self.root = newNode
#             return self.root


#         ptr = self.root
#         while(True):
#             if(data < ptr.data): # go left
#                 if(ptr.left == None):
#                     ptr.left = newNode
#                     return self.root
#                 else:
#                     ptr = ptr.left
#             if(data >= ptr.data): # go right
#                 if(ptr.right == None):
#                     ptr.right = newNode
#                     return self.root
#                 else:
#                     ptr = ptr.right
    
#     def printTree(self, node, level = 0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)

#     def preorder(self,node):
#         if node != None:
#             print(node,end=" ")
#             self.preorder(node.left)
#             self.preorder(node.right)

#     def inorder(self,node):
#         if node != None:
#             self.inorder(node.left)
#             print(node,end=" ")
#             self.inorder(node.right)
    
#     def postorder(self,node):
#         if node != None:
#             self.postorder(node.left)
#             self.postorder(node.right)
#             print(node,end=" ")
    
#     def breadth(self,node):
#         queue = []
#         queue.append(node)
#         while(len(queue) != 0):
#             front = queue[0]
#             queue.pop(0) # pop front
#             if(front != None):
#                 print(front,end=" ")
#                 queue.append(front.left)
#                 queue.append(front.right)     


# T = BST()

# inp = [int(i) for i in input('Enter Input : ').split()]

# for i in inp:
#     root = T.insert(i)

# print("Preorder : ",end="")
# T.preorder(root)
# print("\nInorder : ",end="")
# T.inorder(root)
# print("\nPostorder : ",end="")
# T.postorder(root)
# print("\nBreadth : ",end="")
# T.breadth(root)


# # Expression Tree
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.exp = ['+','-','*','/']
#         self.red = data not in self.exp
    
#     def __str__(self):
#         return str(self.data) + ":" + str(self.red)

# class ExpressionTree:
#     def __init__(self):
#         self.root = None
#         self.exp = ['+','-','*','/']

#     def isRed(self,node):
#         if(node):
#             if(node.data not in self.exp or node.red):
#                 return True
#         return False

#     def makeRed(self,node):
#         if(node.right != None and node.left != None):
#             if(self.isRed(node.right) and self.isRed(node.left) ):
#                 node.red = True
#                 return True
        
#         return False
    
#     def insert(self,node,data):
        
#         if(node == None): # head
#            newNode = Node(data)
#            node = newNode
#            return node

#         if(node.red):
#             return node

#         if(node.right == None): # create right
#             newNode = Node(data)
#             node.right = newNode
#             return node
            
#         if(self.isRed(node.right)):
#             if(node.left != None): # go through
#                 self.insert(node.left,data)
#             else: # create left
#                 newNode = Node(data)
#                 node.left = newNode
#         else:
#             self.insert(node.right,data)

#         self.makeRed(node)
#         return node

#     def printTree(self, node, level = 0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)
    
#     def infix(self,node):
#         if(node != None):
#             if(node.left != None and node.right != None):
#                 print("(",end="")
#             self.infix(node.left)
#             print(node.data,end="")
#             self.infix(node.right)
#             if(node.left != None and node.right != None):
#                 print(")",end="")

#     def prefix(self,node):
#         if node != None:
#             print(node,end="")
#             self.prefix(node.left)
#             self.prefix(node.right)


# pf = input("Enter Postfix : ")

# T = ExpressionTree()
# root = None
# for i in range(len(pf)-1,-1,-1):
#     root = T.insert(root,pf[i])
#     T.printTree(root)
#     print("--------------------------------------------------")
 
# print("Tree :")
# T.printTree(root)
# print("--------------------------------------------------")
# print("Infix : ",end="")
# T.infix(root)
# print()
# print("Prefix : ",end="")
# T.prefix(root)


class Node:
    def __init__(self,index,data):
        self.index = index
        self.interval = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data) + str(self.interval)


class IntervalTree:

    def __init__(self,size):
        self.root = None
        self.size = size
        self.used = 0

    def insert(self,data):
        if(self.root == None):
           self.used += 1
           self.root = Node(self.used,data)
           return self.root
        
        ptr = self.root
        while(ptr != None):
            

