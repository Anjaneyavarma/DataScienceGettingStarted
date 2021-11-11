f = open('file.txt','w')
try:
    with open('file.txt', 'w') as f:
        f.write("My first line \n")
        f.write("My Secod line \n")
        f.write("Contains three line \n")
finally:
    f.close()
