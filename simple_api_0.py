"""
	Example of mini API in Flask
"""


from flask import flask

app = Flask(__name__)

books = [
    {
        "id":1
        "titre" : "un titre"
    },
    {
        "id":2
        "titre" : "un autre titre"
    }
]


@app.route('/')
def home():
	return "This is Flask on your localhost  (: "


@app.route('/route')
def ma_route():
    return"Ceci est une route "


@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books':books})

if __name__ == '__main__':
	app.run()

