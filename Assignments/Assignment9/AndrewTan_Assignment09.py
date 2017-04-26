#Andrew Tan, 4/24, Section 010, Assignment 9

#Open file requested by user
#try:
yes = 1
if yes == 1:
    file = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
    file_obj = open(file+".txt", "r")
    print("Successfully opened {}.txt\n".format(file))
    alldata = file_obj.read()
    student = alldata.split("\n")
    unusable = 0
    answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer = answerkey.split(",")
    grades = []
    student_id = []
    for i in range(len(student)):
        response = student[i].split(",")
        if len(response) != 26:
            unusable += 1
        else:
            #Grading
            student_id.append(response[0])
            del response[0]
            points = 0
            for qn in range(len(response)):
                if response[qn] == answer[qn]:
                    points += 4
                elif response[qn] == "":
                    points += 0
                else:
                    points -= 1
            grades.append(points)

    #Calculate average
    total = 0
    for grd in grades:
        total += grd
    avg = total/len(grades)

    #Calculate median
    ordered_grades = grades
    grades = sorted(ordered_grades)
    if len(grades) % 2 == 0:
        median = (grades[int(len(grades)/2-1)] + grades[int(len(grades)/2)]) / 2
    else:
        median = grades[int((len(grades))/2)]

    #Calculate mode
    count = []
    unique = []
    mode = []
    for x in grades:
        if x not in unique:
            unique.append(x)
            count.append(0)
        for y in grades:
            if x == y:
                loc = unique.index(x)
                count[loc] += 1                
    for unq, cnt in zip(unique, count):
        if cnt == max(count):
            mode.append(unq)
        
    #Display statistics
    print("Grade Summary:")
    print("Total students: {}".format(len(student_id)))
    print("Unusable lines in the file: {}".format(unusable))
    print("Highest score: {}".format(max(grades)))
    print("Lowest score: {}".format(min(grades)))
    print("Mean score: {:.2f}".format(avg))
    print("Median score: {}".format(int(median)))
    print("Mode: {}".format(str(mode)[1:-1].replace(",", "")))
    print("Range: {}".format(max(grades)-min(grades)))

    #Write grades to file
    file_object = open(file+"_grades.txt", "w")
    for student, grd in zip(student_id, ordered_grades):
        file_object.write("{},{:.2f}\n".format(student, float(grd)))
    file_object.close()

    #Curve grades
    curve = str.lower(input("Would you like to curve the exam? 'y' or 'n': "))
    if curve == "y":
        while True:
            desired_mean = float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
            if desired_mean <= avg:
                print("Invalid curve, try again.")
                continue
            else:
                curve = desired_mean - avg
                curved_grades = list(ordered_grades)
                for i in range(len(curved_grades)):
                    curved_grades[i] += curve
                file_object = open(file+"_grades.txt", "w")
                for student, grd, cgrd in zip(student_id, ordered_grades, curved_grades):
                    file_object.write("{},{},{}\n".format(student, int(grd), int(cgrd)+1))
                file_object.close()
                print("Done! Check your grade file!")
                break

#except:
    #print("File cannot be found.")

