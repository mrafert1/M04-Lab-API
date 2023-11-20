from flask import Flask, request
app = Flask (__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE-URI'] = 'sqlite:///data.db'
db = SQLAlchemy (app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(80), unique = True, nullable = False)
    publisher = db.Column(db.String(80), unique = True, nullable = False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index ():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Books.query.all()

    output = []
    for book in books:
        book_data = {'name': book.book_name, 'author': book.author, 'publisher', book.publisher}

        ouput.append(book_data)

    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(["name": drink.name, "description": drink.description])

@app.route('/books', methods =  ['POST'])
def add_book():
    book = Book(book_name = request.json['book_name'], author = request.json['author'], publisher = request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!@"}