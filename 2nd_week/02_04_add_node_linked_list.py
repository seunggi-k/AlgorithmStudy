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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur=self.head
        cur_index=0
        while cur_index != index:
            cur=cur.next
            cur_index+=1
        return cur

    def add_node(self, index, value):
        new_node=Node(value)

        if index==0:
            new_node.next=self.head
            self.head=new_node
            return

        index_minus_1_node=self.get_node(index-1)

        next_node=index_minus_1_node

        index_minus_1_node.next=new_node # 5 -> 7
        new_node.next=next_node # 7 -> 12



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
print(linked_list.get_node(0).data) # -> 5를 들고 있는 노드를 반환해야 합니다!
