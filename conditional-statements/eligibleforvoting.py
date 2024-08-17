# A person eligible for voting or not .

age = int(input("enter age ="))

if(age == 18):
   print("person is eligible for voting")
elif(age>=0 and age<=12):
   print("person is child")
else:
   print("person is not eligible")
