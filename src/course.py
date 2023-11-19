class Course:
    def __init__(self, department, course_code, section_code):
        self.dept = department
        self.courseCode = course_code
        self.sectionCode = section_code

    # Returns True if the two Courses are the same
    def sameCourse(self, otherCourse): 
        if (self.dept == otherCourse.dept) & (self.courseCode == otherCourse.courseCode):
            return True

    # Returns True if the two sections are the same
    def sameSection(self, otherCourse):
        if (self.sectionCode == otherCourse.sectionCode):
            return True

    def sameExactCourse(self, otherCourse):
        if self.sameCourse(otherCourse):
            if self.sameSection(otherCourse):
                return True
            else:
                return False


    
