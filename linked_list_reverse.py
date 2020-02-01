class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linked_list:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            node=self.head
            while node.next is not None:
                node=node.next
            node.next=new_node


    def printh(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp= temp.next

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

llist = linked_list()
llist.insert(20)
llist.insert(4)
llist.insert(15)
llist.insert(85)

llist.reverse()
llist.printh()