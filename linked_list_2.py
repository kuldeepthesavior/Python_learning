class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:

    def __init__(self):
        self.head=None

    def push_at_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def push_at_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else :
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def print_link(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next



llist = linked_list()
llist.push_at_begin(20)
llist.push_at_begin(4)
llist.push_at_begin(15)
llist.push_at_begin(85)

print("insert at begin :\n")
llist.print_link()


llist = linked_list()
llist.push_at_last(20)
llist.push_at_last(4)
llist.push_at_last(15)
llist.push_at_last(85)

print("insert at last :\n")
llist.print_link()


