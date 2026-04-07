class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_sum(self):
        cur=self.head
        sum=0
        while cur is not None:
            sum=sum*10+cur.data
            cur=cur.next
        return sum



def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1=linked_list_1.get_sum()
    sum_2=linked_list_2.get_sum()
    return sum_1+sum_2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))