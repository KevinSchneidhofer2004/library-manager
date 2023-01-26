from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///G:/Schule/INSY Projekt/library-manager/test.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author_name = db.Column(db.String)
    publisher_name = db.Column(db.String)
    release_year = db.Column(db.Integer)
    customer_id = db.Column(db.Integer)


@app.route('/')
def index():
    try:
        books = Book.query.filter_by(author_name='James Dashner').order_by(Book.title).all()
        book_text = '<ul>'
        for book in books:
            book_text += '<li>' + book.title + ', ' + book.author_name + '</li>'
        book_text += '</ul>'
        return book_text
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


app.run(debug=True)
