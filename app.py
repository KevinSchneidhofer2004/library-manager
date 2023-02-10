from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "super secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///G:/Schule/INSY Projekt/library-manager/test.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

Bootstrap(app)
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


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name


@app.route('/')
def index():
    return render_template('index.html', book = Book.query.all())

@app.route('/customers')
def customers():
    return render_template('customers.html', customer = Customer.query.all())

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

@app.route('/new_customer', methods = ['GET', 'POST'])
def new_customer():
   if request.method == 'POST':
      if not request.form['name']:
         flash('Please enter all the fields', 'error')
      else:
         customer = Customer(request.form['name'])
         
         db.session.add(customer)
         db.session.commit()
         
         flash('Record was successfully added')
         return redirect(url_for('customers'))
   return render_template('new_customer.html')

@app.route('/<int:id>')
def RetrieveSingleBook(id):
    book = Book.query.filter_by(id=id).first()
    if book:
        return render_template('book_data.html', book = book)
    return f"Book with id ={id} doesn't exist"

@app.route('/customers/<int:id>')
def RetrieveSingleCustomer(id):
    customer = Customer.query.filter_by(id=id).first()
    book = Book.query.filter_by(customer_id=id).order_by(Book.title).all()
    if customer:
        return render_template('customer_data.html', customer = customer, book = book)
    return f"Customer with id ={id} doesn't exist"

@app.route('/<int:id>/update', methods = ['GET','POST'])
def update(id):
    book = db.session.query(Book).filter(Book.id == id)
    if request.method == 'POST':
        if book:
            book.update({'title': request.form['title'], 'author_name': request.form['author'], 'publisher_name': request.form['publisher'], 'release_year': request.form['release_year']})
            db.session.commit()
            return redirect(f'/{id}')
        return f"Book with id = {id} Doesn't exist"
    return render_template('update.html', book = book)


@app.route('/customers/<int:id>/update', methods = ['GET','POST'])
def update_customer(id): 
    customer = db.session.query(Customer).filter(Customer.id == id)
    if request.method == 'POST':
        if customer:
            customer.update({'name': request.form['name']})
            db.session.commit()
            return redirect(f'/customers/{id}')
        return f"Book with id = {id} Doesn't exist"
    return render_template('update_customer.html', customer = customer)


@app.route('/<int:id>/delete', methods=['GET','POST'])
def Delete(id):
    book = Book.query.filter_by(id=id).first()
    if request.method == 'POST':
        if book:
            db.session.delete(book)
            db.session.commit()
            return redirect('/')
    return render_template('delete.html')


@app.route('/customers/<int:id>/delete', methods=['GET','POST'])
def Delete_Customer(id):
    customer = Customer.query.filter_by(id=id).first()
    if request.method == 'POST':
        if customers:
            db.session.delete(customer)
            db.session.commit()
            return redirect('/customers')
    return render_template('delete.html')


@app.route('/<int:id>/assign', methods = ['GET', 'POST'])
def assign_book(id):
    book = db.session.query(Book).filter(Book.id == id)
    customer = Customer.query.filter_by(name = request.form.get('customer')).first()
    if request.method == 'POST':
        if book:
            if request.form.get('Assignment_Delete'):
                book.update({'customer_id': None})
            elif not request.form['customer']:
                flash('Please enter all the fields', 'error')
            else:
                book.update({'customer_id': customer.id})
            db.session.commit()
            return redirect('/')
    return render_template('book_customer.html')


app.run(debug=True)