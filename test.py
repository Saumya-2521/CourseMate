import pickle
from src.Student import Student
from src.course import Course
pickleFile = "studentList.pickle"

studentList = [
	Student("Max", "maxthestudent@gmail.com", [
		Course("CPSC", "310", "101"),
		Course("CPSC", "320", "102"),
		Course("CPSC", "314", "103"),
		Course("PHIL", "321", "100")
	]),

	Student("Saumya", "saumyathegreat@gmail.com", [
		Course("CPSC", "310", "101"),
		Course("CPSC", "302", "101"),
		Course("MATH", "316", "102"),
		Course("MATH", "317", "105"),
		Course("ENGL", "110", "100")	
	]),

	Student("Navid", "NavidTheGOAT@Gmail.com", [
		Course("CPSC", "322", "101"),
		Course("PSYC", "367", "101"),
		Course("PHIL", "321", "100"),
		Course("PHIL", "351", "101")
	]),

	Student("Bardock", "bardockrules@Outlook.com", [
		Course("CRWR", "200", "101"),
		Course("CPSC", "320", "102"),
		Course("CPSC", "314", "103"),
		Course("PHIL", "321", "100")
	]),

	Student("John Doe", "johhny@yahoo.com", [
		Course("FRST", "200", "101"),
		Course("CPSC", "320", "102"),
		Course("MATH", "314", "103"),
		Course("COMM", "321", "100")
	]),

	Student("Weena Wibowo", "awesomeEmail@gmail.com", [
	]),

	Student("JaMarcus", "JaMarGOAT@Outlook.com", [
		Course("CRWR", "200", "101"), 
		Course("CRWR", "203", "100"),
		Course("CPSC", "103", "102")
	]),

	Student("Tragedeigh", "TragedeighLikesStarbz@Outlook.com", [
		Course("MATH", "221", "102"), 
		Course("MATH", "220", "102"),
		Course("MATH", "215", "100"),
		Course("CPSC", "100", "101")
	]),

	Student("Kayleigh", "Kayleigh1234@Outlook.com", [
		Course("POLI", "100", "101"),
		Course("POLI", "101", "100"),
		Course("HIST", "100", "101")
	]),

]

# # Save to file
# with open(pickleFile, 'wb') as f:
# 	pickle.dump(studentList, f)

# Load from file

with open(pickleFile, 'rb') as f:
	studentList = pickle.load(f)
	print("Loaded from file: ")
	print(studentList)