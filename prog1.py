a =[1,2,3,4,9,8,10,20,40,50,80,90]
l= list()
l.append(a[0])
m=list()
temp=-1
max = a[0]
for i in range(len(a)):
    if i < temp:
        pass
    else:
        for j in range(i+1,len(a)):
            if (a[i] <a[j] and a[j]%a[i]==0 and a[j]>max and a[j]%max==0):
                l.append(a[j])
                m.append(j)
                temp=j
                max = a[j]
                break

print(l)
print(m)
