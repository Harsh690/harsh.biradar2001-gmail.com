# lst = [4,3,2,7,8,9]
# value = 0
# for i in range(1,len(lst)-1):
#     num = 0
#     while num<i:
#         num+=1
#         if lst[i-1]<=lst[i]:
#             for x in range(0,i):
#                 if lst[x]<=lst[i]:
#                    for y in range(lst[i-1],lst[-2]):
#                        if lst[y]>=lst[i]:
#                            print(lst[i])
#                            break
#
#                    break
#                 else: print(-1)
#                 break
#         else: print(-1)
#         break
#-----------------------------------------------------------------------------------------#
# lst = []
# median = 0
# x = int(input())
# for i in range(0,x):
#     num =0
#     n = int(input())
#     lst.append(n)
#     lst.sort()
# if len(lst)%2!=0:
#     median += lst[(x+1)//2-1]
# if len(lst)%2 ==0:
#     median+= ((lst[(x//2)-1]+lst[(x//2)]))//2
# print(median)
#-----------------------------------------------------------------------------------------#
# lst = []
# for i in range(int(input())):
#     median = 0
#     v = int(input())
#     lst.append(v)
#     for x in range(len(lst)):
#        if len(lst)%2!=0:
#            median += lst[(x+1)//2-1]
#            print(median)
#            print(lst)
#        if len(lst)%2 ==0:
#            median+= ((lst[(x//2)-1]+lst[(x//2)]))//2
#            print(median)
#            print(lst)
#            break
#-----------------------------------------------------------------------------------------#
# lst = [1,2,5,-7,2,-5,3]
# first = 0
# second = 0
# for i in range(0,len(lst)):
#     if lst[i]<0:
#         first = lst[0:i]
#         second = lst[i+1:]
#     else:
#         print(lst)
#
# print(first,second)
#-----------------------------------------------------------------------------------------#
# lst = [5,2,1,4]
# num = 9
# def function(lst,num):
#     for i in range(len(lst)):
#        for j in range(len(lst)):
#            if lst[j]+lst[i]==num:
#               print(lst[i],lst[j])
#
#            else:
#              print("NO")
#
# print(function(lst,num))
#-----------------------------------------------------------------------------------------#
# lst = [7,10,4,6,8,10,11]
# x = lst.copy()
# final = []
# num=0
# y = []
# for i in range(len(x)-1):
#     x[i] = x[i+1]-x[i]
# while num<len(x)-1:
#     if x[num+1]==x[num]:
#         final.append(num)
#     if x[num]==x[num-1] and x[num]!=x[num+1]:
#         final.append(num)
#         final.append(num+1)
#     num+=1
#
#
# for i in range(len(final)):
#     y.append(lst[final[i]])
# print(lst)
# print(x)
# print(y)
#-----------------------------------------------------------------------------------------#
# # lst = [4,3,2,1,0]
# lst = [0,5,1,2,4,3]
# final = []
# for i in range(len(lst)):
#     print(lst.index(i),lst[i])
#     final.insert(lst.index(i),lst[i])
# print (final)
#-----------------------------------------------------------------------------------------#
# n = 64
# lst = [1,2,3,4,5,6,7,8,9]
# i= -1
# final= []
# while n >=1:
#     if n%lst[i]==0:
#        n = n/lst[i]
#        final.append(lst[i])
#        print(n)
#     else:
#         i-=1
#         if n ==1:
#             break
# print(final)
#-----------------------------------------------------------------------------------------#
class Hash_Table:
    def __init__(self):
        self.MAX = 100
        self.arr = [[]for i in range(self.MAX)]

    def Hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

        
    def __getitem__(self,key):
        h = self.Hash(key)
        return self.arr[h]
    def __delitem__(self, key):
        h = self.Hash(key)
        pass



t = Hash_Table()
t['march 6'] = 120
t['march 6'] = 78
t['march 8'] = 67
t['march 9'] = 4
print(t)












