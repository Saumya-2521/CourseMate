from flask import Flask, render_template
from src.Student import Student
from src.course import Course
from src.Application import Application

app = Flask(__name__)

@app.route('/')
def test():
	return render_template('index.html')

@app.route('/getRankedList/', methods=['GET'])
def getRankedList():
    # Perform any action you want when this endpoint is called
	# Return python dictionary as specified in Notes.md
    # TODO: Implement this
	mainStud = Student("Max 2", "lavamarmax@gmailc.om", [
		Course("CPSC", "310", "100"),
		Course("CPSC", "320", "102"),
		Course("CPSC", "314", "103"),
		Course("PHIL", "321", "100")
	])
	application = Application()
	return application.getRankedList(mainStud)

@app.route('/signup/')
def signup():
	return render_template('signup.html')

@app.route('/home')
def home():
	return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True) # TODO: Set debug=False before deployment