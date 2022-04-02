# TS-19 04-12-2021

'''Write a python program to concatenate 
following dictionaries to create new one
'''
dic1={1:10,2:20}
dic2={2:35,35:200}
dic3={3:45,6:200}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)
