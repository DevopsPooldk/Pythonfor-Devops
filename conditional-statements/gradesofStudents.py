# Taking marks from student and print its result

marks = int(input("marks of student :"))

if(marks >= 90):
    print("grade A ")
elif(marks >=80 and marks <90):
    print("grade B")
elif(marks >=70 and marks <80):
    print("grade C")
else:
    print("grade D")