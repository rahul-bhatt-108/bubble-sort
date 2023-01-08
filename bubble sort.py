def sort(s):
    s=s
    for i in range(len(s)):

        for k in range(len(s)-i-1):
            #print(f",len(s)={len(s)}, i={i}, len(s)-i-1={len(s)-i-1}, k={k}")
            if s[k]>s[k+1] :
                print(i,k)
                tem=s[k]
                s[k]=s[k+1]
                s[k+1]=tem
                print(s)
    print(s)
a=[1,7,3,4,5,-1]
print(a)
print(sort(a))
