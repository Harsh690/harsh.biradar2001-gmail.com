class itemName:

    def __init__(self,wt,val,i):
        self.wt = wt
        self.val=val
        self.i = i
        self.cost=val/wt

    def __lt__(self, other):#sorts the list on the basis of the val//wt ratio
        return self.cost<other.cost

class knapsack:
    @staticmethod
    def knap(wt,val,capacity):
        lst= []
        for i in range(len(wt)):
            lst.append(itemName(wt[i],val[i],i)) # append the object in the lst
        lst.sort(reverse=True) # sort the lst with respect to the cost
        total_value =0
        q = 0
        for j in lst:
            curr_wt = int(j.wt)
            curr_val = int(j.val)

            while capacity-curr_wt>=0:
                 capacity-=curr_wt        # subtract the weight from capacity
                 total_value+=curr_val

                # increment the total_value with the profit indicating
                #  else:
                #     fraction = capacity/curr_wt  # else divide the capacity with the weight
                #     total_value+= curr_val*fraction
                #     capacity=int(capacity-curr_wt*fraction) # capacity becomes 0
                #     break

        return total_value

if __name__ == '__main__':
    wt = [1,3,4,5]
    val = [1,4,5,7]
    capacity = 8

    maxvalue = knapsack.knap(wt,val,capacity)
    print(maxvalue)