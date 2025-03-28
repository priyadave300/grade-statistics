#results() to convert user input from string to int by using split method and then declaring 2 lists 
#and appending them to grade[0] and grade[1] and also when user_input is empty it will print statistics
#and return and exit from the function
exam_points =[]
exercises =[]
def results():
    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            print (f"Statistics: ")
            return
        else:       
            grade_list = user_input.split(" ")
            exam_points.append(int(grade_list[0]))
            exercises.append(int(grade_list[1]))

# exercise_points function to convert exercise list from 2 digit to single digit and round down using //
# here then declaring convert_exercise_points list to save the single digit exercise point
convert_exercise_points=[]   
def exercise_points():
    for points in exercises:
        points = points //10
        convert_exercise_points.append(points)
    return convert_exercise_points

#points_avg function to print avg of total students. Here we have total_sum calculated by adding exam_points
#with converted exercise points and then creating a array and appending it to total_sum_points/len(exam_points)
total_points_sum =[]
def points_average():
    points_average = 0
    total_points =0
    index =0
    for i in exam_points:
        total_points = i +  convert_exercise_points[index]
        total_points_sum.append(total_points)
        index+=1
    points_average = sum(total_points_sum)/len(exam_points)
    print(f"Points average: {points_average}")

#function to obtain pass % of students. first condition that exam_points is <10 if yes then dont exclude
#only include exam_points >=10 and then add with convert_exercise_points amd see if total_points >14 that means
#append it to pass_list and then divide by len(exam_points)
#also we are appending total_point_list before checking total_points >14 for pass_list abnd also in else 
#appending fail_list for i <10

pass_list =[]
fail_list =[]
total_point_list = []
def pass_percentage():
    index = 0
    for i in exam_points:
        if i >=10:
            total_points = i +  convert_exercise_points[index]
            total_point_list.append(total_points)
            if total_points >14:
                pass_list.append(total_points)
        else:
            fail_list.append(i)

        index+=1
    pass_percent = (len(pass_list)/len(exam_points))*100
    print(f"Pass percentage: {pass_percent:.1f}")

#creating grade function to print out grade from 5 to 0. Here we are calling student_grade(my_list) function 
#whose return value is list by storing it in total_stars variable. total_stars.count will count ith value
#in my_list and print no of stars accordingly
def grade_distribution():
    print("Grade distribution: ")
    total_stars = student_grade(my_list)
    i =5
    while i >=0:
        var = f"{" "*2}{i}{":"} {"*" * (total_stars.count(i))}"
        print(var)
        i =i-1

my_list = []
def student_grade(my_list):
    for grade in total_point_list:
        if 0<=grade<=14:
            my_list.append(0)
        elif 15<=grade<=17:
            my_list.append(1)
        elif 18<=grade<=20:
            my_list.append(2)
        elif 21<=grade<=23:
            my_list.append(3)
        elif 24<=grade<=27:
            my_list.append(4)
        elif 28<=grade<=30:
            my_list.append(5)
    for grade in fail_list:
        if 0<=grade<=14:
            my_list.append(0)
    return my_list

results()
exercise_points()
points_average()
pass_percentage()
grade_distribution()






