# int_min = -12345
# int_max = 12345
#
#
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.right=None
#         self.left=None
#
# def isbst(root,mini,maxi):
#      if root is None:
#          return True
#
#      if root.data>maxi or root.data<mini:
#          return False
#
#      if isbst(root.left,mini,root.data-1) and isbst(root.right,root.data+1,maxi):
#          return True
#
#
# def bst(root):
#     return isbst(root,int_min,int_max)
#
# root = Node(4)
# root.left = Node(2)
# root.right = Node(5)
# root.left.left = Node(1)
# root.left.right = Node(9)
#
# if (bst(root)):
#     print("Is BST")
# else:
#     print("Not a BST")
#
#
#--------------------------------------------------------------------------------------------#
# count = 0
# class Node:
#     def __init__(self,data):
#         self.data= data
#         self.left = None
#         self.right = None
# def bst(root):
#
#     count = 0
#     if root.right:
#         bst(root.right)
#
#     if root.left:
#         bst(root.left)
#
#     if root.left== None and root.right ==None:
#        count+=1
#     print(count)
#     lst.append(count)
# print(lst)
#--------------------------------------------------------------------------------------------#
# CODING QUESTION : - TO count LEAF Nodes
#
# from queue import Queue
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = self.right = None
#
#
# def getleaf(node):
#     if node is None:
#         return 0
#
#
#     q = Queue()
#     q.put(node)
#     count = 0
#     while (not q.empty()):
#         temp = q.queue[0]
#         q.get()
#         if temp.left!=None:
#             q.put(temp.left)
#
#         if temp.right!=None:
#             q.put(temp.right)
#
#         if temp.right ==None and temp.left ==None:
#             count+=1
#
#     return count
#
#
# if __name__ == '__main__':
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)

    # get leaf count of the above
    # created tree
   # print(getleaf(root))
#-------------------------------------------------------------------------------------------
# CODING QUESTION FOR PRINTING FULL NODES IN A TREE
# class Node:
#     def __init__(self,data):
#         self.data= data
#         self.right=None
#         self.left=None
#
#
#
# def full_node(root):
#     if root:
#        if root.left and root.right:
#           print(root.data,end=" ")
#        full_node(root.right)
#        full_node(root.left)
#
#
# if __name__ == '__main__':
#     root = Node(10)
#     root.left = Node(8)
#     root.right = Node(2)
#     root.left.left = Node(3)
#     root.left.right=Node(5)
#     root.right.left = Node(7)
#     root.right.right = Node(6)
#     root.right.left.right = Node(7)
#     root.right.right.right = Node(8)
#     root.right.left.right.left = Node(9)
#
#     full_node(root)
#-------------------------------------------------------------------------------------------
# CODING QUESTION TO CALCULATE HEIGHT OF A BINARY TREE
# class Node:
#
#     def __init__(self,data):
#         self.data = data
#         self.right = None
#         self.left=None
#
#
# def maxDepth(root):
#     if root==None:
#         return 0
#
#     else:
#         left =maxDepth(root.left)
#         right = maxDepth(root.right)
#         if left>right:
#             left+=1
#             return left
#         else:
#             right+=1
#             return right
#
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# # root.right.left=Node(3)
# # root.left.left = Node(4)
# # root.left.right = Node(5)
#
# print("Height of tree is %d" % (maxDepth(root)))
#-------------------------------------------------------------------------------------------
# CODING QUESTION TO PRINT NUMBERS AT K DISTANCE
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None
#
# def sum(root,k):
#     if root is None:
#         return
#
#     if k==0:
#         print(root.data)
#     else:
#         sum(root.left, k - 1)
#         sum(root.right, k - 1)
#
#
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(8)
#
# sum(root, 2)
#-------------------------------------------------------------------------------------------
# string = 'jsbr qmj u y vjo ue krmd ssviq tid'
# final = []
# lst = list(string)
# final.append(lst[0])
# for i in range(len(lst)):
#     if lst[i-1]==' ':
#         final.append(lst[i])
# result = ''
# for i in final:
#     result+=i
# print(final)
# print(result)
#-------------------------------------------------------------------------------------------
# string = 'zvvo'
# lst = list(string)
# final = []
# for i in range(len(lst)):
#     if lst[i] in final:
#         pass
#     else:
#         final.append(lst[i])
#
# result = ''
# for i in range(len(final)):
#     result+=final[i]
# print(result)
#-------------------------------------------------------------------------------------------
# lst = 'bac'
# arr = list(lst)
# arr.sort()
# print(arr)
#------------------------------------------------------------------------------------------
# lst = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
# dictionary= {}
# occur=[]
# num = 9948
# i=0
# while i<len(lst):
#      if num>=lst[i]:
#          dictionary[lst[i]] = num // lst[i]
#          num = num - lst[i]*(num//lst[i])
#          i+=1
#      else:
#          i+=1
#
#      if num==lst[-1]:
#          dictionary[lst[i]]=num//lst[i]
#          break
# print(dictionary)
#------------------------------------------------------------------------------------------
# from itertools import combinations
# lst = [1,2,2]
# i=0
# final=[]
# while i <len(lst)+1:
#     var = list(combinations(lst,i))
#     final+=(var)
#     i+=1
# print((final))
#------------------------------------------------------------------------------------------
# string = 'hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs'
# lst = list(string)
# for i in range(len(lst)):
#     if lst.count(lst[i])==1:
#         print(lst[i])
#         break
#     if i==-1:
#         print(-1)
#------------------------------------------------------------------------------------------
# arr = [11, 5, 3, 4, 3, 5, 6]
# # print(list(arr))
#
# def function(arr,n):
#     i = 0
#     for i in range(len(arr)):
#        i += 1
#        if arr.count(arr[i]) >= 2:
#          return(i + 1)
#          break
#     if i == len(arr):
#       return (-1)
#
# print(function(arr,len(arr)))
#------------------------------------------------------------------------------------------
# lst = [2,2,2,2]
# i=0
# arr=[]
# def function(arr,lst,i):
#     for i in range(len(lst)):
#         arr.append(lst.count(lst[i]))
#     for j in range(len(arr)):
#         if arr[j]==1:
#             return lst[j]
#         else:
#             return -1
#
# print(function(arr,lst,i))
#------------------------------------------------------------------------------------------
# def function(a,n):
#     a = set(a)
#     a= list(a)
#     print(a)
#     for i in range(n):
#         if a[0]and a[1]:
#            return a[0],a[1]
#         else:
#             return -1
#
# a = [1,2,1,3,6,7]
# n= len(a)
# print(function(a,n))
# print(n)
#----------------------------------------------------------------------------------------
# arr = [-1,-2,-3,-4]
# max_so_far =max_ending_here =0
# for i in range(len(arr)):
#     max_ending_here= max_ending_here+arr[i]
#     if max_ending_here>max_so_far:
#         max_so_far= max_ending_here
#     if max_ending_here<0:
#         max_ending_here=0
# print(max_so_far)
# #----------------------------------------------------------------------------------------
# def displaysublist(A):
#     # store all the sublists
#     B = [[]]
#
#     # first loop
#     for i in range(len(A) + 1):
#         # second loop
#         for j in range(i + 1, len(A) + 1):
#             # slice the subarray
#             sub = A[i:j]
#             B.append(sub)
#     return B
#
#
# # driver code
# A = list()
# n = int(input("Enter the size of the First List ::"))
# print("Enter the Element of First List ::")
# final = []
# var = 0
# new = []
# for i in range(int(n)):
#     k = int(input(""))
#     A.append(k)
#     var = displaysublist(A)
# for i in range(len(var)):
#     final.append(var[i])
# for j in range(len(final)):
#    new.append(sum(final[j]))
# print(new)
# print(max(new))
# #----------------------------------------------------------------------------------------
# from itertools import permutations
# string = 'ABCB'
# perm = permutations(string)
# lst = []
# for i in list(perm):
#     var = "".join(i)
#     lst.append(var)
#
# var = set(lst)
# print(len(var))
# #----------------------------------------------------------------------------------------
# lst =[2,4,6,8,10,12,14,16,18,20]
# j =8
# var = slice(0,j)
# remaining_array = slice(j,lst[-1])
# new = lst[var]
# remaining = lst[remaining_array]
# for i in range(len(new)):
#     remaining.append(new[i])
# print(remaining)
# #----------------------------------------------------------------------------------------
# def permutation(lst):
#    if len(lst)==0:
#      return []
#
#    if len(lst)==1:
#        return [lst]
#    l = []
#    for i in range(len(lst)):
#        m = lst[i]
#
#        rem_list=lst[:i]+lst[i+1:]
#
#        for p in permutation(rem_list):
#           l.append([m] + p)
#    return l
#
#
# data = list('123')
# for p in permutation(data):
#     print (p)
#----------------------------------------------------------------------------------------
# val = [60,100,120]
# W = 50
# weight=[10,20,30]
# val_to_weight_ratio=[]
# lst = [1,1,2/3]
# final = 0
# for i in range(len(val)):
#     val_to_weight_ratio.append(val[i]/weight[i])
#     final +=val[i]*lst[i]
#
# print(final)
#----------------------------------------------------------------------------------------
# N = 4
# string = '**d**d8*ffd8*f8d8f*FD**F***8F8*'
# lst = list(string)
# count = 0
# def function(N,lst,count):
#     for i in range(len(lst)):
#        if lst[i]=='*':
#            count+=1
#            if count>=N:
#               break
#        else:
#           count=0
#     if count>=N:
#       return ('Yes')
#     else:
#       return ('No')
#
# print(function(N,lst,count))
#----------------------------------------------------------------------------------------
# def sub_lists(l):
#     lists = [[]]
#     for i in range(len(l) + 1):
#         for j in range(i):
#             lists.append(l[j: i])
#     return lists
#
#
# k= int(input())
# l1 = [2,2,2,2,2,2]
# var = sub_lists(l1)
# var.pop(0)
# count = 0
# new = []
# for i in range(len(var)):
#     if sum(var[i])%k==0:
#         count+=1
#
# print(count)
#-----------------------------------------------------------------------------------------
# def n_length_combo(lst, n):
#     if n == 0:
#         return [[]]
#
#     l = []
#     for i in range(0, len(lst)):
#
#         m = lst[i]
#         remLst = lst[i + 1:]
#
#         for p in n_length_combo(remLst, n - 1):
#             l.append([m] + p)
#
#     return l
#
#
# # Driver code
# if __name__ == "__main__":
#     arr = "abc"
#     print(n_length_combo([x for x in arr], 2))
# def find(n, m):
#     # for quotient
#     q = n // m
#     print("Quotient: ", q)
#
#     # for remainder
#     r = n % m
#     print("Remainder", r)
#
#
# # Driver Code
# find(3, 3)
# find(3, 3)
#-----------------------------------------------------------------------------------------
# S = 'defRTSersUXI'
# lst = list(S)
# small = []
# large = []
#
# for i in range(len(lst)):
#     if lst[i]>='a' and lst[i]<='z':
#         small.append(lst[i])
#
#     if lst[i]>='A' and lst[i]<='Z':
#         large.append(lst[i])
# small.sort()
# large.sort()
# x = 0
# y=0
# for j in range(len(lst)):
#     if lst[j]>='a' and lst[j]<='z':
#         lst[j]=small[x]
#         x+=1
#
#     if lst[j]>='A' and lst[j]<='Z':
#         lst[j]=large[y]
#         y+=1
#
# new = ''.join(lst)
# print(new)
#-----------------------------------------------------------------------------------------
# lst =['baoyal','bmmdgq']
# # lst = ["cat", "dog", "tac", "god", "act"]
# new = []
# def hash(string):
#     h=0
#     for char in string:
#         h+=ord(char)
#     return h
#
# for i in range(len(lst)):
#     var = hash(lst[i])
#     new.append(var)
#
# dict = {}
#
# for i in range(len(new)):
#     dict.setdefault(new[i], [])
#     dict[new[i]].append(lst[i])
#
# for i in dict.values():
#     print(i)
# print(hash(lst[0]))
#-------------------------------------------------------------------------------
# lst = ['for','geeks','geeks']
# dict={}
# max_val =0
# final = []
# for i in lst:
#      if i in dict:
#          dict[i]+=1
#      else:
#          dict[i]=1
# for key,value in dict.items():
#     if value>=max_val:
#         max_val=value
#         final.append(key)
#
# for key,values in dict.items():
#     if values ==max_val:
#         print(final)
#-------------------------------------------------------------------------------

var = 2

def function(x,y):
    print(var)

x = 0
y=0
function(x,y)






