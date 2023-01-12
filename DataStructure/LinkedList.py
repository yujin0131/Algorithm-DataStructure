class Node:                   # Node 클래스 정의
    def __init__(self, data): # __init__ (constructor) 초기화 함수 > 인스턴스화 할 때 반드시 처음에 호출됨.  ( 블로그 정리 필요 )
        self.data = data      # self : 인스턴스 자신 > constructor는 필수로 첫 인수를 self로 지정해야함
        self.next = None      # .next() : 다음 노드 search

# Create LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    # print LinkedList
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): # _ : 값이 딱히 상관없을 경우 언더스코어(_)로 표시 
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        temp.value = value
        return True

    def insert(self, index, value):
        # if index < 0 or index >= self.length:
        #     return None
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)

        newNode = Node(value) # 받아온 노드
        temp = self.get(index - 1) # 원래 해당 index 값 temp 노드에 옮김
        newNode.next = temp.next # 원래 index.next 를 newNode.next 에 옮김
        temp.next = newNode # temp.next 에 새로운 newNode

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst
        if index == self.length - 1 :
            return self.pop
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        


