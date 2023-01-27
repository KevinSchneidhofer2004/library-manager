from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "super secret key"

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

    def __init__(self, title, author_name, publisher_name, release_year):
        self.title = title
        self.author_name = author_name
        self.publisher_name = publisher_name
        self.release_year = release_year


@app.route('/')
def index():
    return render_template('index.html', book = Book.query.all())

@app.route('/new_book', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['title'] or not request.form['author'] or not request.form['publisher'] or not request.form['release_year']:
         flash('Please enter all the fields', 'error')
      else:
         book = Book(request.form['title'], request.form['author'],
            request.form['publisher'], request.form['release_year'])
         
         db.session.add(book)
         db.session.commit()
         
         flash('Record was successfully added')
         return redirect(url_for('index'))
   return render_template('new_book.html')


@app.route('/<int:id>')
def RetrieveSingleEmployee(id):
    book = Book.query.filter_by(id=id).first()
    if book:
        return render_template('book_data.html', book = book)
    return f"Book with id ={id} doesn't exist"


@app.route('/<int:id>/update', methods = ['GET','POST'])
def update(id):
    book = Book.query.filter_by(id=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit()
            title = request.form['title']
            author = request.form['author']
            publisher = request.form['publisher']
            release_year = request.form['release_year']
            book = Book(id=id, title=title, author_name=author, publisher_name=publisher, release_year=release_year)
            db.session.add(book)
            db.session.commit()
            return redirect(f'/{id}')
        return f"Book with id = {id} Doesn't exist"
 
    return render_template('update.html', book = book)


@app.route('/<int:id>/delete', methods=['GET','POST'])
def Delete(id):
    book = Book.query.filter_by(id=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit()
            return redirect('/')
    return render_template('delete.html')



app.run(debug=True)
