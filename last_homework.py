
for i in range (0,3):
    name=input("Enter your Name and Surname: ")
    if name=="Hakan Yesilyurt":
        print("Welcome")
        break
    elif i==3 and name!="Hakan Yesilyurt":
        print("Please try again later.")
        exit()

courses=[]
for k in range(0,5):
    lesson=input("Enter the lesson you want to take (if you don't want to take more lessons, press Q): ")
    if lesson.upper()=="Q":
        break
    else:
        courses.append(lesson)
if len(courses)<3:
    print("You failed in a class.")
chosen_course=input("Enter the course you want to take exams: ")
midterm_grade=input("Enter your Midterm Grade: ")
final_grade=input("Enter your Final Grade: ")
project_grade=input("Enter your Project Grade: ")
course={"Course Name":chosen_course,"Midterm":midterm_grade,"Final":final_grade,"Project":project_grade}
total_grade=int(course["Midterm"])*0.3+int(course["Final"])*0.5+int(course["Project"])*0.2

if total_grade>= 90 :
    print(f"You got AA from \"{chosen_course}\" course")
elif total_grade>=70 and total_grade<90:
    print(f"You got BB from \"{chosen_course}\" course")
elif total_grade>=50 and total_grade<70:
    print(f"You got CC from \"{chosen_course}\" course")    
elif total_grade>=30 and total_grade<50:
    print(f"You got CC from \"{chosen_course}\" course")    
elif total_grade<30:
    print(f"You got FF from \"{chosen_course}\" course. You have failed, please work harder next time.")    
    

