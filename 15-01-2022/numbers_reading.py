# TS 19 15-01-2022
'''
Write a Python program to 
read an entire text file.'''

def read():
    file=open(r"number.txt",'r')
    print(file.read())
    file.close()
read()