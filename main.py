import random
rl = mylist = list(dict.fromkeys(random.sample(range(10, 100), 20)))
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def Inorder(root): 
    if root:
        Inorder(root.left) 
        print(root.data,end=" "), 
        Inorder(root.right)

def Preorder(root): 
    if root: 
        print(root.data,end=" "), 
        Preorder(root.left) 
        Preorder(root.right)  
               
def Postorder(root): 
    if root: 
        Postorder(root.left) 
        Postorder(root.right) 
        print(root.data,end=" "),

def printLevelOrder(root): 
    h = height(root) 
    for i in range(1, h+1): 
        printGivenLevel(root, i) 
  
def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print(root.data,end=" ") 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 

def height(node): 
    if node is None: 
        return 0 
    else : 
        lheight = height(node.left) 
        rheight = height(node.right) 

        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1

def ifNodeExists(node, key): 
  
    if (node == None):  
        return False
  
    if (node.data == key):  
        return True
  
    res1 = ifNodeExists(node.left, key)  
    if res1: 
        return True
    res2 = ifNodeExists(node.right, key)

root=Node(80)
for ll in rl:
	root.insert(ll)



while True:
	print("\nOptions:\n[1] Preorder\n[2] Inorder\n[3] Postorder\n[4] Levelorder\n[5] Search a node")
	try:
            c=int(input("Input choice: "))
            if c==1:
                print("\nPreorder:")
                Preorder(root)
            elif c==2:
                print("Inorder:")
                Inorder(root)
            elif c==3:
                print("\nPostorder:")
                Postorder(root)
            elif c==4:
                print("\nLevelorder:")
                printLevelOrder(root)
            elif c==5:  
                key= int(input("Enter node to Search : "))
                if (ifNodeExists(root, key)):  
                    print("The value was found ") 
                else: 
                    print("There is no value")
	except ValueError:
            print("\n--Invalid input--\n--Try Again--")

	cc=input("\nDo you want to try again Y/N ")
	if cc=='y' or cc=='Y':
		    continue 
	elif cc=='N' or cc=='n':
            print("\n--Program Exit--")
            break
	else :
            print("\n--Invalid input--\n--Try Again--")
            continue