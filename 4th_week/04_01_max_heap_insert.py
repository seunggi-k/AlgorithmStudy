class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value): #시간 복잡도 O(logN)
        self.items.append(value)
        #               cur
        #   0    1      2
        # [None, 4,    9]

        cur_index=len(self.items)-1
        while cur_index !=1:
            # 부모 노드랑 비교해서 내가 더 크다면 위치를 바꿈
            parent_index=cur_index//2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index]= self.items[parent_index], self.items[cur_index]
                cur_index=parent_index
            else :
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!