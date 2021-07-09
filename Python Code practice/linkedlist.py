class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,val):
        Node = node(val,self.head)
        self.head = Node

    def insert_at_end(self,data):
        if self.head ==None:
            self.head=node(data,None)

        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next= node(data,None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def print(self):
        if self.head ==None:
            print("Linkedlist is empty")
            return
        itr = self.head
        lstr = ""
        while itr:
            lstr+=str(itr.data)+ "-->" if itr.next else str(itr.data)
            itr=itr.next
        print(lstr)

    def insert_values(self,datalist):
        self.head=None
        for data in datalist:
            self.insert_at_end(data)

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            print("Error")

        if index ==0:
            self.insert_at_beginning(data)

        else:
            count = 0
            itr = self.head
            while itr:

                if count== index-1:
                    Node = node(data,itr.next)
                    itr.next = Node
                    break
                itr = itr.next
                count += 1

    def remove_at(self,index):
        if index<0 or index>self.get_length():
            print("Error")

        else:
            count = 0
            itr = self.head
            while itr:
                if count==index-1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count+=1



if __name__ == "__main__":
    lst = linkedlist()
    lst.insert_values(["banana", "mango", "grapes", "orange"])

    lst.print()
    lst.insert_at(1,'Jackfruit')
    lst.remove_at(2)
    lst.print()








