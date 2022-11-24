#project
names=input("enter names:")
name_list=names.split(",")
marks=input("enter marks:")
marks_list=marks.split(",")
d=dict(zip(name_list,marks_list))
print(d)
marks2=input("enter the updated marks: ")
mark2_list=marks2.split(",")
new_marks=[]
for i in range(0,len(marks_list)):
    new_marks=int(marks_list[i])+int(mark2_list[i])
max=max(new_marks)
d2=dict(zip(str(new_marks),name_list))
for x,y in d2.items():
    if x==max(d2):
        print("maximum marks is got by:",y,"and marks is:",max)
