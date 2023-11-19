from Student import Student
import pickle

class Application:
	PICKLE_FILE = "studentList.pickle"
	def __init__(self):
		# Load list of students from file
		self.studentList = self.loadStudentList()

	# @return the final list of ranked students for a given student
	def getRankedList(self, student):
		# TODO
		pass

	# Creates a list of students from a file
	# @return a list of students
	def loadStudentList(self):
		try:
			with open(self.PICKLE_FILE, 'rb') as f:
				return pickle.load(f)
		except FileNotFoundError:
			return []