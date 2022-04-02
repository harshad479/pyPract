# TS-19 04-12-2021

'''Write a python program to 
sum all items in dictionary'''

def return_sum(dictt):
    sum=0
    for i in dictt.values():
        sum+=i
    return sum

# driver function
d={'a':100,'b':200,'c':300}
print("sum : ", return_sum(d))