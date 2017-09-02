def find(big):
    i=100
    while (i<=big) :
        whole=str(i)
        if i == int(whole[0])**3 + int(whole[1])**3 + int(whole[2])**3:
            print (i,sep=' ')
        i+=1
    else:
        pass

find(999)

##testing file changes