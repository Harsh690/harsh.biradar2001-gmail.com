maxi = 12345
mini = -12345
class Node:
    def __init__(self,data):
        self.data=data
        self.right = None
        self.left = None

def isbst(elements):
    new = bst(mini,maxi,elements)
    return new
def bst(mini,maxi,root):
    if root is None:
        return True

    if  root.data>maxi or root.data<mini:
        return False
    # if root.left:
    #     if not bst(mini,root.data+1,root.left):
    #         return False
    # if root.right:
    #     if not bst(root.data,maxi,root.right):
    #         return False

    if bst(mini,root.data-1,root.left) and  bst(root.data+1,maxi,root.right):
       return True



root = Node(5)
root.left = Node(1)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(6)

if isbst(root):
    print("is Bst")

else:
    print("Not A bST")