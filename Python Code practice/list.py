class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class linkedlist:

    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        if self.head==None:
            new_node =node(data,None)
            self.head=new_node

        else:
            itr = self.head
            while itr.next:
                itr=itr.next
            itr.next = node(data,None)


    def add_elements(self,elements):
        self.head = None
        for i in elements:
            self.insert_at_end(i)

    def print(self):
        if self.head ==None:
            return ("list is empty")
        itr = self.head
        stri = ""
        while itr:
            stri+=str(itr.data) + "-->" if itr.next else str(itr.data)
            itr = itr.next
        print (stri)
final = 0
def list(l1,l2,final):
    itr1 = l1.head
    itr2 = l2.head
    while min(len(lst1),len(lst2)):
        if str(itr1) +str(itr2) ==15:
            final+=1
            if itr1.next:
                itr1=itr1.next
            itr2=itr2.next
        if str(itr1.data)+str(itr2.data)>=15:
            itr2 = itr2.next

        else:
            itr1 = itr1.next
if __name__ =='__main__':
    lst1 = [1,2,3,4,5,6]
    lst2 = [11,12,13]
    l1 = linkedlist()
    l1.add_elements(lst1)

    l2 = linkedlist()
    l2.add_elements(lst2)
    l1.print()
    l2.print()
    print(list(l1,l2,final))
    print(final)