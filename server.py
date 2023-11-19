from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test():
	return render_template('index.html')

@app.route('/getRankedList/', methods=['GET'])
def getRankedList():
    # Perform any action you want when this endpoint is called
	# Return python dictionary as specified in Notes.md
    # TODO: Implement this
	return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True) # TODO: Set debug=False before deployment