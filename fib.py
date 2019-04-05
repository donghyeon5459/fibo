n1 =1
n2 = 1
n3 =0
num = input("input number : ")

if( num == 1 or num == 2 ):
    print "1"

else:
    for i in range(0,num-2):
        n3=n1+n2
        n1=n2
        n2=n3
    print n3