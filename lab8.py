# # ถั่ว
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
#             print("*",end="")
#             return self.root
        

#         ptr = self.root
#         while(True):
#             if(data < ptr.data): # go left
                
#                 if(ptr.left == None):
#                     print("L",end="")
#                     print("*",end="")
#                     ptr.left = newNode
#                     return self.root
#                 else:
#                     ptr = ptr.left
#                     print("L",end="")
#             if(data >= ptr.data): # go right
#                 if(ptr.right == None):
#                     print("R",end="")
#                     print("*",end="")
#                     ptr.right = newNode
#                     return self.root
#                 else:
#                     ptr = ptr.right
#                     print("R",end="")
    
#     def printTree(self, node, level = 0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)
  

# T = BST()

# inp = [int(i) for i in input('Enter Input : ').split()]

# for i in inp:
#     root = T.insert(i)
#     print()


# # Ranking
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.height = 1

#     def __str__(self):
#         return str(self.data)  

    

# class AVL:

#     def __init__(self):
#         self.root = None

#     def rotateLeft(self,node):  
#         old = node
#         newhead = node.right
#         newheadOldLeft = node.right.left

#         old.right = newheadOldLeft
#         node = newhead
#         node.left = old

#         self.updateHeight(node.left)
#         self.updateHeight(node)
#         return node

#     def rotateRight(self,node):  
#         old = node
#         newhead = node.left
#         newheadOldRight = node.left.right

#         old.left = newheadOldRight
#         node = newhead
#         node.right = old

#         self.updateHeight(node.right)
#         self.updateHeight(node)
#         return node

#     def getHeight(self,node):
#         if(not node):
#             return 0
        
#         return node.height
     
#     def Balance(self,node):
#         if(node == None):
#             return False
        
#         return self.getHeight(node.left) - self.getHeight(node.right) 


#     def insert(self,node,data):
#         if(not node):
#           return  Node(data)
        
#         ptr = node

#         if(data < ptr.data): # go left
#             node.left = self.insert(node.left,data)
#             node.height += 1
         
#         if(data >= ptr.data): # go right
#             node.right = self.insert(node.right,data)
#             node.height += 1
         
        
#         self.updateHeight(node)

#         balance  = self.Balance(node)


#         if(balance > 1 and data >= node.left.data): # left right
#             node.left = self.rotateLeft(node.left)

#         if(balance > 1): # left left
#             return self.rotateRight(node)

#         if(balance < -1 and data < node.right.data): # right left
#             node.right = self.rotateRight(node.right)

#         if(balance < -1): # right right
#             return self.rotateLeft(node)

#         return node


     

#     def updateHeight(self,node):
#         node.height = max(self.getHeight(node.left),self.getHeight(node.right)) + 1         

#     def printTree(self, node, level = 0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)


# T = AVL()

# inp = [int(i) for i in input('Enter Input : ').split()]
# root = None
# for i in inp:
#     print("Insert : (",i,")")
#     root = T.insert(root,i)
#     T.printTree(root)
#     print("--------------------------------------------------")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.height = 1
    
#     def __str__(self):
#         return str(self.data)  

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self,node, data):

#         if(not node):
#             return Node(data)

#         if(data >= node.data):
#             node.right = self.insert(node.right,data)
#         else:
#             node.left  = self.insert(node.left,data)

#         self.updateHeight(node)
#         return node
        


#     def updateHeight(self,node):
#         node.height =  self.getHeight(node.left) + self.getHeight(node.right) + 1

#     def getHeight(self,node):
#         if(not node):
#             return 0
        
#         return node.height    
    
#     def printTree(self, node, level = 0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)
  
#     def find(self,root,data):
        
#         if(not root):
#             return 0
#         ptr = root
#         s   = 0
#         while(ptr != None):
#             if(data == ptr.data):
#                 return s + self.getHeight(ptr.left) + 1
#             if(data > ptr.data): # go right
#                 if(not ptr.right):
#                     return s + self.getHeight(ptr.left) + 1
#                 s  += self.getHeight(ptr.left) + 1
#                 ptr = ptr.right
                

#             if(data < ptr.data): # go left
#                 if(ptr.left != None and data <= ptr.left.data):
#                     ptr = ptr.left
#                 else:
#                     if(ptr.left == None):
#                         return  s
#                     elif(data > ptr.left.data):
#                         return  self.getHeight(ptr) - self.getHeight(ptr.left) - 1
            
                        
#         return s
         


# T = BST()

# raw = input('Enter Input : ').split("/")

# [inp,val] = raw
# val = int(val)
# inp = [int(i) for i in inp.split()]
# root = None
# for i in inp:
#     root = T.insert(root,i)

# T.printTree(root)
# print("--------------------------------------------------")
# print("Rank of",val,":",T.find(root,val))

# def getSymbol(a,b):
#     if(a > b):
#         return ">"
#     elif(a < b):
#         return "<"
#     else: 
#         return "="

# [tree,inp] = input("Enter Input : ").split("/")

# tree = [int(i) for i in tree.split()]

# print(sum(tree))

# for i in range(len(tree)-1,-1,-1):
#     ind = i
#     value = tree[ind]
#     ind =  ind // 2 - (ind + 1) % 2
#     if(ind < 0):
#         continue
#     tree[ind] += value

# for i in inp.split(","):
#     l,r = [int(ind) for ind in i.split()]
#     print(l,getSymbol(tree[l],tree[r]),r,sep="")

 
class Node:
    
    def __init__(self, data): 

        self.data = data  

        self.left = None  

        self.right = None 

        self.level = None 



    def __str__(self):

        return str(self.data) 



class Tree:

    def __init__(self): 

        self.root = None

        self.num = 0



    def insert(self, val):  

        if self.root == None:

            self.root = Node(val)

            self.num += 1

        else:

            h = height(self.root)

            max_node = pow(2,h+1)-1

            current = self.root

            if self.num+1 > max_node:

                while(current.left != None):

                    current = current.left

                current.left = Node(val)

                self.num+=1

            elif self.num+1 == max_node:

                while(current.right != None):

                    current = current.right

                current.right = Node(val)

                self.num+=1

            else:


                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)

                else:

                    insert_subtree(current.right,self.num - pow(2,h),val)

                self.num+=1

                    

def insert_subtree(r,num,val):

    if r != None:

        h = height(r)

        max_node = pow(2,h+1)-1

        current = r

        if num+1 > max_node:

            while(current.left != None):

                current = current.left

            current.left = Node(val)

            return

        elif num+1 == max_node:

            while(current.right != None):

                current = current.right

            current.right = Node(val)

            return

        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

            insert_subtree(current.left,num - round(pow(2,h)/2),val)

        else:

            insert_subtree(current.right,num - pow(2,h),val)

    else:

        return



def height(root):

    if root == None:

        return -1

    else:

        left = height(root.left)

        right = height(root.right)

        if left>right:

            return left + 1

        else:

            return right + 1

                       

def printTree90(node, level = 0):

    if node != None:

        printTree90(node.right, level + 1)

        print('     ' * level, node)

        printTree90(node.left, level + 1)


INT_MAX = 4294967295
INT_MIN = -4294967295
def check_binary_search_tree_(root,mini = INT_MIN ,maxi = INT_MAX):
    if root is None: 
        return True
  
    # False if this node violates min/max constraint 
    if root.data < mini or root.data > maxi: 
        return False
    
    if root.data < 0 or root.data > 100:
        return False

    # Otherwise check the subtrees recursively 
    # tightening the min or max constraint 
    return (check_binary_search_tree_(root.left, mini, root.data -1) and
          check_binary_search_tree_(root.right, root.data+1, maxi)) 

tree = Tree()

data = input("Enter Input : ").split()

for e in data:

    tree.insert(int(e))

printTree90(tree.root)

print(check_binary_search_tree_(tree.root))