# TS 19 15-01-2022
'''
Write a Python program to write text
 in a file and display the text'''
def main():
    output=open(r"cricketer.txt",'w')
    output.write('Sachin Tendulkar\n')
    output.write('Sourav Ganguli\n')
    output.write('Rahul Dravid\n')
    output.close()
main()

def read():
    file=open(r"cricketer.txt",'r')
    print(file.read())
    file.close()
read()