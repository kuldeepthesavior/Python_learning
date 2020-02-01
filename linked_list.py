class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

def insertatlast (root, node):
    if root is None:
        root=node
    else:
        link=root
        while link.next is not None:
            link=link.next
        link.next=node







def printh(root):
    while root is not None:
        print(root.data)
        root=root.next


for i in range(10):
    if i==0 :
        r=Node(0)
    else:
        insertatlast(r, Node(i))




# r=Node(1)
# insert(r,Node(2))
# insert(r,Node(3))
# insert(r,Node(4))
# insert(r,Node(5))
# insert(r,Node(6))
print("at last insertion : \n")
printh(r)

print("at begin insertion : \n")
printh(r)