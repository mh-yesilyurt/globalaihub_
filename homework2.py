FirstName=input("Enter Your First Name: ")
LastName=input("Enter Your Last Name: ")
Age=input("Enter Your Age: ")
birth=input("Enter Your Year of Birth: ")

infos=[FirstName.title(),LastName.title(),Age,birth]
for i in range(4):
     print(infos[i],end=" ")
print("\n")
if int(Age)>=18 and 2020-int(birth)>=18:
    print("You can go out to the street")
else:
    print("You can't go out because it's too dangerous.")


