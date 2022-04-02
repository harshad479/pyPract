# TS 19 15-01-2022
'''
Write a Python program to append text 
to a file and display the text'''
def writeData():
    output=open(r"number.txt",'a')
    output.write('''
544\n454\n56\n656\n565\n54\n49''')
    output.close()
    print("DONE")
writeData()

def read():
    file=open(r"number.txt",'r')
    print(file.read())
    file.close()
read()
