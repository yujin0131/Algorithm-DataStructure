class Node:                   # Node 클래스 정의
    def __init__(self, data): # __init__ (constructor) 초기화 함수 > 인스턴스화 할 때 반드시 처음에 호출됨.  ( 블로그 정리 필요 )
        self.data = data      # self : 인스턴스 자신 > constructor는 필수로 첫 인수를 self로 지정해야함
        self.next = None      # .next() : 다음 노드 search

# Create LinkedList
class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
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

    def pop(self, value):
        newNode = Node(value)
        if self.length == 0:
            return None
        temp = newNode
        pre = self.head
        self.head.next = pre
        

# node1 = Node(3)

# print(node1.data)
# print(node1.next)