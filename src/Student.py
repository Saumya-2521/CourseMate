from src.course import Course

class Student:
    def __init__(self, name, email, courses):
        self.name = name
        self.email = email
        self.courseList = courses
    
    # @return a number above 0, denoting similarity between a student and self
    def getOtherStudentPoints(self, otherStudent):
        points = 0
        for course in (self.courseList):
            for otherStudentCourse in (otherStudent.courseList):
                points += course.sameExactCourse(otherStudentCourse)
        return points




#
# (CPSC 310, CPSC 320)
# (CRWR 200, LING 100, CPSC 310, CPSC 320)
#
#