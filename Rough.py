a=[1,2,3,4,5]
sum=0
    if (a==""):
        print("None")
    else:
        if(len(a)%2!=0):
            for i in range(len(a)):
            #median=sum/len(a)
            #print(median)
                sum=a[i]+sum
                median=sum/len(a)
            print(median)
        for i in range(len(a)):
            sum=(a[len(a)/2] + a[len(a)/2+1])+sum
            median=sum/2
    print(median)