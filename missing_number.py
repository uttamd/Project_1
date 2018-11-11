l=  [5,1,3,4,7,2]
l.sort()
i=0
#print(len(l))

while True:
     #i=0
     if l[i]-l[i+1]==1:
         i+=1
     if (l[i]-l[i+1])>1:
        print('missing number',l[i+1])
        break
     if i == len(l)-2:
        break





