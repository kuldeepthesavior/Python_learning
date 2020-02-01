class Node:
    def __init__(self,key):
        self.data=key
        self.l_child=None
        self.r_child=None

def insert(root , node):
    if root is None:
        root=node
    else:
        if root.data<node.data:
            if root.r_child is None:
                root.r_child=node
            else :
                insert(root.r_child,node)
        else:
            if root.l_child is None:
                root.l_child=node
            else:
                insert(root.l_child,node)

def inrder(root):
    if root:
        inrder(root.l_child)
        print(root.data)
        inrder(root.r_child)

def postorder(root):
    if root:
        postorder(root.l_child)
        postorder(root.r_child)
        print(root.data)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.l_child)
        preorder(root.r_child)




r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

# Print inoder traversal of the BST
print("printing inorder traversal : \n")
inrder(r)


print("printing preorder traversal : \n")
preorder(r)

print("printing postorder traversal : \n")
postorder(r)

