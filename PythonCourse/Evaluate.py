x, y, z = map(int,input().split())
total = x+y+z
if(x>=40 and y>=40 and z>=40):
    if( x+y >=120):
        print("Eligible", total)
    elif(y+z>=120):
        print("Eligible", total)
    elif(z+x>=120):
        print("Eligible", total)
    else:
        print("Not Eligible", total)
else:
    print("Not Eligible", total)