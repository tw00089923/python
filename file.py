
#import sys 

#print(sys.path)


a = open("hi.txt","r",encoding="utf-8")
lists = a.readlines()

for list in lists :
    print(list)


    