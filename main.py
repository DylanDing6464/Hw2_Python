def getGradePoint(letterGrade):
  if(letterGrade == "A"):
    return 4.0
  elif (letterGrade == "A-"):
    return 3.67
  elif (letterGrade == "B+"):
    return 3.33
  elif (letterGrade == "B"):
    return 3.0
  elif (letterGrade == "B-"):
    return 2.67
  elif (letterGrade == "C+"):
    return 2.33
  elif (letterGrade == "C"):
    return 2.0
  elif (letterGrade == "D"):
    return 1.0
  else:
    return 0.0

def run():
	c1letterGrade = input("Enter your course 1 letter grade: ")
	credit1 = float(input("Enter your course 1 credit: "))
	gradepoint1 = getGradePoint(c1letterGrade)
	print(f"Grade point for course 1 is: {gradepoint1}")
	
	
	c1letterGrade = input("Enter your course 2 letter grade: ")
	credit2 = float(input("Enter your course 2 credit: "))
	gradepoint2 = getGradePoint(c1letterGrade)
	print(f"Grade point for course 2 is: {gradepoint1}")


	c1letterGrade = input("Enter your course 3 letter grade: ")
	credit3 = float(input("Enter your course 3 credit: "))
	gradepoint3 = getGradePoint(c1letterGrade)
	print(f"Grade point for course 1 is: {gradepoint3}")


	gpa = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3)/(credit1 + credit2 + credit3)

	print(f"Your GPA is: {gpa}")

if __name__ == "__main__":
	run()