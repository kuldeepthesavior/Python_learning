class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def  mirror(node):
    if node is None:
        return
    else :
        temp=node
        mirror(node.left)
        mirror(node.right)

        temp=node.left
        node.left=node.right
        node.right=temp

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

if __name__ == '__main__':

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    print("before mirror : \n")



    inorder(root)
    mirror(root)
    print("after mirror : \n")
    inorder(root)