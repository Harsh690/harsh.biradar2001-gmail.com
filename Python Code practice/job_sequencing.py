# class itemName:
#     def __init__(self,id,deadline,profit):
#         self.profit = profit
#         self.deadline = deadline
#         self.id = id
#
#     def __lt__(self, other):
#         return self.profit<other.profit
#
#
# class job_sequencing:
#     @staticmethod
#     def job(id,deadline,profit):
#         lst = []
#         for i in range(len(id)):
#             lst.append(itemName(id[i],deadline[i],profit[i]))
#
#         new_lst = set(lst)
#         print(new_lst)
#         lst.sort(reverse=True)
#         max_deadline = max(deadline)
#
#         max_profit = 0
#         ids=[]
#         for j in lst:
#             curr_profit = int(j.profit)
#             if max_deadline>=1:
#                 max_profit+=curr_profit
#                 ids.append(j.deadline)
#
#
#
#             max_deadline-=1
#             if max_deadline<1:
#                 break
#         return max_profit
#
# if __name__=="__main__":
#     id = [1,2,3,4]
#     deadline = [4,1,1,1]
#     profit = [20,10,40,30]
#     print(job_sequencing.job(id,deadline,profit))

def printJobScheduling(arr, t):
    # length of array
    n = len(arr)

    # Sort all jobs according to
    # decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    result = [False] * t
    

arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

printJobScheduling(arr, 3)