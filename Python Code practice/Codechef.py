# CODING PROBLEM NO 1 RATIONAL NUMBERS

# n = int(input())
# lst = []
# while n>=1:
#     for num in range(1,n+1):
#        pass
#     for x in range(1,n):
#        var = x/num
#        if var<1:
#           lst.append(var)
#     n-=1
# new = set(lst)
# print(len(new))
# *--------------------------------------------------------------------------------*

# CODING PROBLEM NO 2 SWEETS


# for __ in range(int(input())):
#     n = int(input())
#     lst = []
#     for _ in range(n):
#        number = int(input())
#        lst.append(number)
#     notes = int(input())
#     y = sum(lst)//notes
#     z =y*notes
#     minimum = min(lst)
#     if sum(lst) -minimum > z:
#        print(-1)
#     else:
#        print(y)

# *--------------------------------------------------------------------------------*
# lst = [1,2,4,4,6,6]
# var = 0
# current = 0
# lenth = len(lst)
# while current<lenth-1:
#     lol = abs(lst[current+1]-lst[current])
#     if lol<=2 and lol>0:
#         var+=1
#         current+=2
#     else: current+=1
# print(var)

# *--------------------------------------------------------------------------------*
# n,p= map(int,input().split())
# lst = []
# for _ in range(0,n):
#    number = int(input())
#    lst.append(number)
#    var = max(lst)
# for num in range(0,len(lst)):
#     lst[num] = lst[num]-var
#     lst[num] = lst[num]*(-1)
# print(lst)
# *--------------------------------------------------------------------------------*
# lst = [5,5,2]
# x = 0
# for num in range(len(lst)-2):
#   if lst[num]==lst[num+1]==lst[num+2]:
#      x =1
#   else: pass
#
#
# if x ==1:
#   print('YES')
# else:
#   print('No')
# *--------------------------------------------------------------------------------*

# lst= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# lst.sort()
# lst1 = []
# for num in range(len(lst)-1):
#     if lst[num][1]==lst[num+1][1]:
#         lst1.append(lst[num][0])
#         lst1.append(lst[num+1][0])
#
#
# print(lst1)

# *--------------------------------------------------------------------------------*
# for _ in range(int(input())):
#     n = list(map(str,input()))
#     while len(n)%2 ==0:
#        for num in range(0,len(n)-2,1):
#            if n[num]==n[num+1]:
#              if n[num+1]=='R' and n[num+2]=='G':
#                 n[num+1],n[num+2]=n[num+2],n[num+1]
#                 break
#              elif n[num+1] =='G' and n[num+2] =='R':
#                  n[num+2], n[num+1] = n[num+1], n[num+2]
#                  break
#            break
#        for sun in range(len(n)-1):
#           if n[sun] ==n[sun+1]:
#              print('No')
#              break
#           elif n[sun] ==n[sun-1]:
#              print('No')
#              break
#           else:
#                print('Yes')
#                break
#        break
# *--------------------------------------------------------------------------------*
# lst = []
# new_lst =[]
# sun = 0
# final = []
# l= 1
# n= 0
#
# while l<2:
#    l+=1
#    for num in range(n,l):
#        if sun<=l:
#           lst.append(sun)
#           sun+=1
#           new_lst = lst[::-1]
#           new_lst.pop(0)
#           new =  lst +new_lst
#           final = final+new
#        n+=1
# print(final)
# *--------------------------------------------------------------------------------*
# for _ in range(int(input())):
#    lst = list(map(int,input()))
#    def function(lst):
#       var = sum(lst)
#       floor = var//9
#       min = floor*9
#       max = min+9
#       if (var - min)> (max-var):
#          difference = max-var
#          return (difference)
#       elif (var - min)< (max-var):
#            summ = var - min
#            return (summ)
#    print(function(lst))
# *--------------------------------------------------------------------------------*
# number = int(input())
# times = int(input())
# var = 0
# lst = []
# lst.append(0)
# for i in range(0,4):
#    x= 0
#    for j in range(0,i):
#        x=x+1
#        lst.append(x)
#    for y in range(0,i):
#        x=x-1
#        lst.append(x)
# for num in range(len(lst)):
#     if lst[num]==number:
#         var+=1
#         if var==times:
#             print(num)
# *--------------------------------------------------------------------------------*
# lst = ['blue','yellow','green','orange','black','green']
# var = 0
# lst.sort()
# for num in range(len(lst)-2):
#     if lst[num]==lst[num+1]==lst[num+2]:
#         var+=3
#
# if var==3:
#     print('Yes')
# else:
#     print('NO')
# *--------------------------------------------------------------------------------*
# knowledge = N and Power = M knowlegde = X and power = Y
# for _ in range(int(input())):
#    N,M,X,Y = map(int,input().split())
#
#    def funtion(N,M,X,Y):
#       knowledge = 1
#       power = 1
#       if N-knowledge ==1 and M-power ==1:
#          return('Chefirnimo')
#
#       var_1 = N//X
#       mult_1 = var_1 *X
#       knowledge+=mult_1
#
#       var_2 = M//Y
#       mult_2 = var_2 *Y
#       power+=mult_2
#
#       if N ==knowledge and M ==power:
#          return ('Chefirnimo')
#       elif N - knowledge ==1 and M - power==1:
#          return ('Chefirnimo')
#       else:
#          return('Pofik')
#    print(funtion(N,M,X,Y))
# *--------------------------------------------------------------------------------*
# lst = []
# lst1 = []
# s = [3,7,9,11]
# x = 0
# for num in range(0,5):
#     for _ in range(0,5):
#        var = input()
#        lst.append(var)
#     for sun in range(len(lst)):
#         k = lst.index('K')
#         p = lst[sun]
#         if lst[sun]=='P':
#              final = abs(k-sun)
#              lst1.append(final)
#
#
# set_1 = set(lst1)
# exact_list = list(set_1)
# for num in range(len(exact_list)):
#     number = exact_list[0]
#     y = abs(exact_list[num]-number)
#     if y in s:
#         x+=1
# print(x)
# *--------------------------------------------------------------------------------*
# from itertools import combinations
# for _ in range(int(input())):
#    length = int(input())
#    lst = list(map(int,(input().split())))
#    lst1 = []
#    x = 0
#    y = 1
#    while x<=len(lst):
#       for num in range(x,len(lst)):
#          z = lst[x:y]
#          lst1.append(z)
#          y+=1
#       x+=1
#    lst2 = []
#    for i in range(len(lst1)):
#       final = sum(lst1[i])
#       lst2.append(final)
#
#    new_lst2 = max(set(lst2))
#    final_list = lst1[lst2.index(new_lst2)]
#
#    x = min(final_list)
#    if len(final_list)<=1:
#       print(sum(final_list))
#    else:
#       final_list.remove(x)
#       print(sum(final_list))
# *--------------------------------------------------------------------------------*
# import collections
# lst = [1,2,2,3,3]
# var = 0
# odd_list = []
# even = []
# new = collections.Counter(lst)
# new_lst = list(new.values())
# for num in range(len(new_lst)):
#     if new_lst[num]%2 ==0:
#        even.append(new_lst[num])
#
#     if new_lst[num]%2!=0 or new_lst[num]%2==1:
#         odd_list.append(new_lst[num])
# var+=sum(even)
# if sum(odd_list)>0:
#   var+=sum(odd_list)-1
# else:
#     var+=sum(odd_list)
#
# print(var)
# *--------------------------------------------------------------------------------*
# import math
# n = int(input())
# x = 0
#
# lst = []
# lst1 = []
# C=0
# def function(C,x,n):
#    while math.pow(2,x) <n:
#         x+=1
#         lst.append(x)
#         lst1.append(math.pow(2,x))
#
#    diffrence_1 = math.pow(2,x)-n
#    diffrence_2 = abs(math.pow(2,x-1) -n)
#    if diffrence_1>diffrence_2:
#        x -=1
#    final_diffrence = abs(n - math.pow(2,x))
#
#
#    for num in range(len(lst1)):
#        C += 1
#        if lst1[num] ==n:
#            return(0)
#
#        else:
#            final_diffrence_1 = final_diffrence + C
#            final_diffrence_2 = final_diffrence - C
#            if lst1[num] == final_diffrence_1:
#                 return(C)
#            if lst1[num] == final_diffrence_2:
#                return(C)

# print(function(C,x,n))
# *--------------------------------------------------------------------------------*
# import math
# lst = []
# lst1 = [0,0,4]
# x= 0
# while x<len(lst1):
#     lst.append(math.pow(2,x))
#     x+=1
# y = lst1[-2]
# final = lst1 [-1]
# index1 = lst1.index(final)
#
# if abs(y*2-lst[index1])==final:
#     print("YES")
# else:
#     print("No")
# *--------------------------------------------------------------------------------*
# x= list(map(int,input().split()))
#
# final = 0
# def convert(list):
#     s = [str(i) for i in list]
#     res = int("".join(s))
#     return (res)
# for z in x:
#    for num in range(z):
#       y = list(map(int, str(num)))
#       Reverse = y[::-1]
#       var = convert(Reverse)
#       if num  + var ==z:
#           final +=1
#           break
#       else:
#         pass
# print(final)
# *--------------------------------------------------------------------------------*
# B = 6
# N = 14
# var = 0
# final = 0
# def code(B,N,var,final):
#     if B == 1:
#       for num in range(0,N//2):
#         var+=1
#         new = (N -var)
#         final = new*var
#     elif B <N//2:
#       for i in range(0,(N//2)-1):
#          var+=1
#          new = (N - var)/B
#          final = new*var
#     else :
#         return (B)
#     return final
#
# print(code(B,N,var,final))
# *--------------------------------------------------------------------------------*
# import itertools
# lst = [-5,4,1,2]
# for i in range(len(lst)):
#     var  = lst[0]
#     lst.pop(0)
#     lst.append(var)
#     print(lst)
#     def allSubArrays(lst):
#        n = len(lst)
#        indices = list(range(n+1))
#        for i,j in itertools.combinations(indices,2):
#           yield lst[i:j]
#     if lst[i]<=0:
#         lst.pop(lst[i])
#     print(sum(max(list(allSubArrays(lst)))))
# *--------------------------------------------------------------------------------*
# lst = [4,7]
# n = lst[::-1]
# A = 0
# def number(n,A):
#    while sum(n)!=2:
#      while n[0]>n[1]:
#         A+=1
#         n[0] = n[0]-n[1]
#      while n[0]<n[1]:
#        A+=1
#        n[1] = n[1] - n[0]
#    if A%2 ==0:
#      return("NO")
#    if sum(n)>2:
#       return("NO")
#    else:
#      return("Yes")
#
# print(number(n,A))
# *--------------------------------------------------------------------------------*
# first = int(input())
# last = int(input())
# final = 0
# for i in range(first-1,last+1):
#     lst = list(map(int, str(i)))
#     v = 0
#     for num in range(len(lst)):
#         if lst[num] ==4 or lst[num]==7:
#             v+=1
#     if v == 4:
#         final+=1
# print(final)
# *--------------------------------------------------------------------------------*

# lst=list(map(int,input().split()))
# k = int(input())
# lst.sort()
# N = int(input())
#
# for num in range(N):
#     if len(lst)%2 == 0:
#         if num<=(len(lst)//2)-1:
#             lst[num]+=k
#         else:
#             lst[num]-=k
#     if len(lst)%2!=0:
#         if num < len(lst)//2:
#           lst[num]+=k
#         else:
#             lst[num]-=k
# mini = lst[0]
# maxi= lst[-1]
#
# print(maxi - mini)

# *--------------------------------------------------------------------------------*
# new = 'uddudduuud'
# lst = list(new)
#
# new = 0
# slope = 0
# final = 0
# unichar = 0
# if lst[0] == 'd':
#     slope -= 1
# if lst[0] == 'u':
#     slope += 1
# for i in range(len(lst)):
#     unichar+=1
#     if lst[i]=='d':
#         new-=1
#     elif lst[i]=='u':
#         new+=1
#     if new == slope:
#         if lst[unichar-1]=='d':
#            final+=1
# print(final)
# print(lst)
# print(new)
# print(slope)
# *--------------------------------------------------------------------------------*
# N,M,T= input().split()
# aircraft =[]
# camps = []
# id = []
# for _ in range(int(N)):
#     x,y,ID = input().split()
#     aircraft.append([int(x),int(y),int(ID)])
# for _ in range(int(M)):
#     x,y,ID = input().split()
#     camps.append([int(x),int(y),int(ID)])
#
# print(aircraft)
#
# print(camps)
# *--------------------------------------------------------------------------------*
# lst = [4,4,4,0,0]
# new = min(lst)
# lst.pop(lst.index(new))
# for i in range(len(lst)):
#     lst[i] = lst[i]-new
# print(sum(lst))
# *--------------------------------------------------------------------------------*
# string_name = "pidedsjfbjsdafpifsfpifapi"
# lst = list(string_name)
# for i in range(len(lst)-1):
#     if lst[i]=='p' and lst[i+1]=='i':
#         lst[i]= lst[i]+lst[i+1]
#         lst[i+1]=''
# for j in range(len(lst)):
#     if lst[j]=="pi":
#         lst[j]='3.14'
# print(lst)
# new = ''.join(lst)
# print(new)
# *--------------------------------------------------------------------------------*
#
# class BST:
#     def __init__(self,data):
#         self.data = data
#         self.right = None
#         self.left = None
#
#
#     def addchild(self,val):
#         if val>self.data:
#             if self.right:
#                 self.right.addchild(val)
#             else:
#                 self.right = BST(val)
#         if val < self.data:
#             if self.left:
#                 self.left.addchild(val)
#             else:
#                 self.left = BST(val)
#
#         if val == self.data:
#             return
#
#     def traverse(self):
#         lst = []
#
#         if self.right:
#             lst+= self.right.traverse()
#         if self.left:
#             lst+= self.left.traverse()
#
#         lst.append(self.data)
#
#         return lst
# def build(elements):
#     root = BST(elements[0])
#     for i in range(1,len(elements)):
#         root.addchild(elements[i])
#     return root
#
# if __name__ == "__main__":
#     # numbers = ["india","UK","USA","Sweden"]
#     numbers = [10,5,15,3,7,13,18,1,6]
#     # numbers = [1,3,2]
#     tree = build(numbers)
#     final = tree.traverse()
#     output = 0
#     final.sort()
#     print(final)
#     var = 0
#     lst=[]
#     for i in range(len(final)-1):
#         lst.append(abs(final[i]-final[i+1]))
#     print(min(lst))
# *--------------------------------------------------------------------------------*
# input = ['c','c','e','e','a','b','a', 'c','d']
# set =list(set(input))
# lst = []
# for i in range(len(set)):
#     v =input.count(set[i])
#     lst.append(v)
# print(set,lst)
# string = 'cceeabacd'
# lst = tuple(string)
# # dictionar={'c':2,'e':1,'a':1,'b':1,'z':1}
# dictionar={'c':2,'e':2,'d':1,'t':1,'g':1,'k':1}
# # ccefeekgtddf
# y = list(dictionar.values())
#
# print(y)
# palindrome = 0
#
# for i in range(len(y)):
#     if y[i]>2:
#         palindrome+=y[i]//3
#         y[i]= y[i]- (y[i]//3*3)
#     else:
#         pass
#
# if y.count(2)==1:
#     palindrome+=1
# elif y.count(2)<y.count(1):
#     palindrome+=y.count(2)
# else:
#     palindrome+=sum(y)//3
# print(palindrome)
# *--------------------------------------------------------------------------------*
# lst = []
# def printSubArrays(arr, start, end):
#     # Stop if we have reached the end of the array
#     if end == len(arr):
#         return
#
#     # Increment the end point and start from 0
#     elif start > end:
#         return printSubArrays(arr, 0, end + 1)
#
#         # Print the subarray and increment the starting
#     # point
#     else:
#         lst.append(arr[start:end + 1])
#         return printSubArrays(arr, start + 1, end)
#
#     # Driver code
#
#
# arr = [3,3,9,9,5]
# printSubArrays(arr, 0, 0)
# final = []
# for i in range(len(lst)):
#     v =sum(lst[i])%7
#     final.append(v)
# print(max(final))
# *--------------------------------------------------------------------------------*
# class Node:
#
#     def __init__(self,data):
#         self.data=data
#         self.right = None
#         self.left = None
#         self.ans = None
#
#     def addchild(self,val):
#         if self.data ==None:
#             self.data = Node(val)
#         if self.data>val:
#             if self.left:
#                self.left.addchild(val)
#             else:
#                 self.left = Node(val)
#         if self.data<val:
#             if self.right:
#                 self.right.addchild(val)
#             else:
#                 self.right = Node(val)
#
#     def traversal(self):
#         lst = []
#         if self.left:
#             #going left
#             lst+= self.left.traversal()
#             # visiting main node
#         lst.append(self.data)
#
#             #going right
#         if self.right:
#             lst+= self.right.traversal()
#
#         return lst
#     def function(self,L,H):
#         lst = []
#         if Node:
#             if L<self.data<H:
#                lst.append(self.data)
#
#             if L>self.data:
#                 # self.function(self.left)
#
#             if L<self.data:
#                 self.right.function(L,H)
#
#         return lst
#
# bst = Node(10)
# bst.addchild(5)
# bst.addchild(15)
# bst.addchild(3)
# bst.addchild(7)
# bst.addchild(18)
#
#
# print(bst.function(7,15))
# print(bst.traversal())
#------------------------------------------------------------------------------------------------#
# def ally(n):
#     val = 0
#     if n<10:
#         return n
#
#     if n>10:
#         for i in range(1,n+1):
#            res = [int(x) for x in str(i)]
#            number = res[0]
#
#            res.sort()
#            final = set(res)
#            new = list(final)
#            if number==new[0]:
#                val+=1
#
#            # strings = [str(res) for res in res]
#            # a_string = "".join(strings)
#            # integer = int(a_string)
#            # if i<integer or i ==integer:
#            #    val+=1
#     return val
# print(ally(500))
#-------------------------------------------------------------------------------------------------


















