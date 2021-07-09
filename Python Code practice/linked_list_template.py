class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def addbegin(self,data):
        node = Node(data,self.head)
        self.head = node

    def insertatend(self,data):
        if self.head is None:
            self.head = Node(data,None)

        else:
            count = 0
            itr = self.head
            while itr.next:
                count+=1
                itr = itr.next

            itr.next = Node(data,None)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_index(self,data,index):
        if index ==0:
            return self.addbegin(data)

        if index <0 and index>=self.length():
            raise ("Index exceeding")

        else:
          count = 0
          itr = self.head
          while itr:
              if count+1 ==index:
                  node= Node(data,itr.next)
                  itr.next = node
                  break
              itr= itr.next
              count+=1

    def insert_values(self,datalist):
        self.head=None
        for data in datalist:
            self.insertatend(data)

    def print(self):
        lststr = ""
        if self.head is None:
            return ("Empty")

        else:
            itr = self.head
            while itr:
                lststr+=str(itr.data) + "-->"
                itr=itr.next

            print(lststr)

    def delete(self,data):
        curr_node= self.head
        if curr_node and curr_node.data==data:
            self.head=curr_node.next
            curr_node=None
            return
        prev =None
        while curr_node and curr_node.data!=data:
             prev=curr_node
             curr_node=curr_node.next

        if curr_node is None:
            return
        prev.next=curr_node.next
        curr_node=None

    def delete_at_index(self,pos):
        curr_node=self.head
        if pos==0:
            self.head=curr_node.next
            curr_node=None
            return


        count=0
        prev=None
        while curr_node and count!=pos:
            count+=1
            prev=curr_node
            curr_node=curr_node.next

        if curr_node is None:
            return

        prev.next=curr_node.next
        curr_node=None

    def get_element(self,data):
        itr = self.head
        while itr.next and itr.data!=data:
            itr=itr.next
        if itr.data ==data:
            return itr
        else:
            return None

def occurence(root,search_for):
    itr = root.data
    count=0
    while itr:
        if itr==search_for:
            count+=1
        itr=itr.next
        print(count)




def delete_with(root):
    next_var = root.next
    root.data=next_var.data
    root.next=next_var.next
    return
if __name__ == "__main__":
    l1 = linkedlist()
    l1.insert_values([2,2,3,2,2])
    l1.print()
    # l1.delete('Mango')
    # l1.delete_at_index(3)
    to_delete= l1.get_element(2)
    delete_with(to_delete)
    l1.print()
    print(occurence(2))














