## **Student** class 
should have String: name, String: email, courses: Course[]

Student.getRankedList(): returns a list of students in order of ranking:
```
OGSTUDENT (EXAMPLE): 
"name": "Saumya",
"email": "lookinggood@gmail.com",
"course":
	- CPSC310 101
	- CPSC320 101
	- MATH400 100



[
	{
		"name": "Max"
		"email": lavamarmax@gmail.com,
		"courses": [
			{
				"dept": "CPSC",
				"code": "310",
				"section": "101",
				"sameSection": true,
			},
			{
				"dept": "CPSC",
				"code": "320",
				"section": "102",
				"sameSection": false,
			}
		]
	},
	{
		"name": "Navid"
		"email": dumbass@gmail.com,
		"courses": [
			{
				"dept": "CPSC",
				"code": "310",
				"section": "101",
				"sameSection": true,
			}
		]
	}
]
```

getOtherStudentPoints(): returns a number above 0, denoting the similarity between two students.

## **Course** class should have:

dept, : string,
code : string,
section-code: string,


## Point values
- same course, same section: 2
- same course diff section: 1
- other: 0

pros:
	- less room for error
	- One course per week handling
cons:
 - boring
 - user may not know section num off the top of their head

# weekdays: "M/W/F" || "Tu/Th",
time: "13:00"

 pros:
  - good for nice ui in future
  - impressive
cons: 
 - more room for error
 - more typing for user
 - more implementation


