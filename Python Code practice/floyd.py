class Node:
    def __init__(self,data):
        self.data =data
        self.next =None



class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

class solution:
     def detect_loop(self,data):
        slow_p=data
        fast_p=data
        while(slow_p and fast_p and fast_p.next):
           slow_p=slow_p.next
           fast_p= fast_p.next.next
           if slow_p==fast_p:
              return True
           else:
              return False


llist = LinkedList()
llist.push(1)
llist.push(3)
llist.push(4)
lst= []

# Create a loop for testing
llist.head.next.next = llist.head.next
if (solution().detect_loop(llist.head)):
    print("Found Loop")
else:
    print("No Loop")