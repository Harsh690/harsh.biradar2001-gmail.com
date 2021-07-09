# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def addchild(self,child):
#         child.parent=self
#         self.children.append(child)
#
#     def level(self):
#         l = 0
#         p = self.parent
#         while p:
#             l+=1
#             p = p.parent
#         return l
#
#     def print(self):
#         count = " " * self.level()
#         state = count+"|-" if self.level() else""
#         print(state+self.data)
#
#         if self.children:
#             for child in self.children:
#                 child.print()
#
# def build():
#     root = Node("Games")
#
#     Fps = Node("Fps")
#     Fps.addchild(Node("COD MW2"))
#     Fps.addchild(Node("COD MW3"))
#     Fps.addchild(Node("COD MWW"))
#     Fps.addchild(Node("COD Ghosts"))
#
#     Stealth = Node("Stealth")
#     Stealth.addchild(Node("AC Revelations"))
#     Stealth.addchild(Node("AC Unity"))
#     Stealth.addchild(Node("AC Rogue"))
#     Stealth.addchild(Node("AC Ghosts"))
#
#     root.addchild(Fps)
#     root.addchild(Stealth)
#     return root
# if __name__ =='__main__':
#     root = build()
#     root.print()
#--------------------------------------------------------------------------------#
class binary:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def addchild(self,data):
        if data == self.data:
            return
        else:
            if data < self.data:
                if self.left:
                    self.left.addchild(data)
                else:
                    self.left = binary(data)

            if data > self.data:
                if self.right:
                    self.right.addchild(data)
                else:
                    self.right = binary(data)

    def sum(self):
        left_sum = self.left.sum() if self.left else 0
        right_sum = self.right.sum() if self.right else 0
        return self.data +left_sum+right_sum

    def pre_order_traversal(self):
        lst = []
        lst.append(self.data)

        if self.left:
            lst+=self.left.pre_order_traversal()

        if self.right:
            lst+=self.right.pre_order_traversal()

        return lst

    def post_order_traversal(self):
        lst = []
        if self.left:
            lst+=self.left.post_order_traversal()

        if self.right:
            lst+=self.right.post_order_traversal()
        lst.append(self.data)
        return lst

    def traversal(self):
        lst = []
        count=0
        #in-order traversal
        if self.left:
            # left elements
            lst+=self.left.traversal()
        #node elements
        lst.append(self.data)

        if self.right:
            # right elements
            lst+=self.right.traversal()

        if self.right ==None and self.left ==None:
            count+=1
        return count

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def delete(self,val):
        if val > self.data:
            if self.right:
                self.right=self.right.delete(val)
        elif val <self.data:
            if self.left:
                self.left= self.left.delete(val)

        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            min = self.right.find_min()
            self.data=min
            self.right = self.right.delete(min)

        return self

    def size(self):
        if self.data is None:
            return 0
        else:
            left= self.size()


def build(lst):

    root = binary(lst[0])

    for i in range(1,len(lst)):
        root.addchild(lst[i])

    return root

if __name__ =='__main__':
    elements = [2,7,6,5,9,2,6]
    tree= build(elements)
    print(tree.sum())








