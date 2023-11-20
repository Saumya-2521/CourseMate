from src.Student import Student
import pickle

class Application:
	PICKLE_FILE = "studentList.pickle"
	def __init__(self):
		# Load list of students from file
		self.studentList = self.loadStudentList()

	# @return the final list of ranked students for a given student
	def getRankedList(self, student):
		# TODO
		
		points = []
		# Get points for every student
		for i in range(len(self.studentList)):
			points.append(self.studentList[i].getOtherStudentPoints(student))

		# Make a dictinary of points (as value) and student names as key
		studentPointsDict = {}
		for i in range(len(self.studentList)):
			studentPointsDict[self.studentList[i].name] = points[i]

		# Sort the dictionary by points
		sortedStudentPointsDict = dict(sorted(studentPointsDict.items(), key=lambda item: item[1], reverse=True))

		# Make the actual dictionary of students, according to notes.md   
		rankedList = []
		for i in range(len(sortedStudentPointsDict)):
			keysNamesOfStudents = list(sortedStudentPointsDict.keys())
			
			for oneStudent in self.studentList:
				if oneStudent.name == keysNamesOfStudents[i]:
					rankedObject = {}
					rankedObject["name"] = oneStudent.name
					rankedObject["email"] = oneStudent.email
					rankedObject["courses"] = self.selectCourseList(oneStudent, student)
					rankedList.append(rankedObject) 
		return rankedList

	
 	# @returns the list of courses that the student has in common with the other student
	def selectCourseList(self, student, otherStudent):
		# Make a list of courses that the student and otherStudent have in common
		# Return that list
		sameSectionList = []
		sameCourseList = []
		for course in otherStudent.courseList:
			for studentCourse in student.courseList:
				if (course.sameExactCourse(studentCourse) == 2):
					sameSectionList.append(course)
					break
				elif (course.sameExactCourse(studentCourse) == 1):
					sameCourseList.append(course)
					break

		selectedCourseList = []
		for course in sameSectionList:
			courseObj = {}
			courseObj["department"] = course.dept
			courseObj["courseCode"] = course.courseCode
			courseObj["sectionCode"] = course.sectionCode
			courseObj["sameSection"] = True
			selectedCourseList.append(courseObj)

		for course in sameCourseList:
			courseObj = {}
			courseObj["department"] = course.dept
			courseObj["courseCode"] = course.courseCode
			courseObj["sectionCode"] = course.sectionCode
			courseObj["sameSection"] = False
			selectedCourseList.append(courseObj)

		return selectedCourseList


	# Creates a list of students from a file
	# @return a list of students
	def loadStudentList(self):
		try:
			with open(self.PICKLE_FILE, 'rb') as f:
				return pickle.load(f)
		except FileNotFoundError:
			return []