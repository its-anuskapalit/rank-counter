import calendar
a=input("enter the first date")
a1=a.split("/")
start=int(a1[2])
b=input("enter the first date")
b1=b.split("/")
end=int(b1[2])
print("the range is: from",start,"to",end)
leap=[]
nonleap=[]
for i in range(start,end+1):
    if(calendar.isleap(i)==False):
        leap.append(i)
    else:
        nonleap.append(i)
print("list of leap year is:",leap)
print("list of non leap year is:",nonleap)
