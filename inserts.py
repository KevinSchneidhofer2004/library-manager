from book import Book
from base import Session, engine, Base
from customer import Customer

Base.metadata.create_all(engine)

session = Session()

harry_potter = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Bloomsburry Publishing", 1995)
lord_of_the_rings = Book("Lord Of The Rings", "J.R.R. Tolkien", "Allen & Unwin", 1935)
maze_runner = Book("The Maze Runner", "James Dashner", "Delacorte Press", 2009)
scorch_trials = Book("The Scorch Trials", "James Dashner", "Delacorte Press", 2010)

uwe_boll = Customer("Uwe Boll")
heinz_honzl = Customer("Heinz Honzl")
josef_feff = Customer("Josef Feff")

uwe_boll.book.append(maze_runner)
uwe_boll.book.append(scorch_trials)
heinz_honzl.book.append(lord_of_the_rings)
josef_feff.book.append(harry_potter)

session.add(harry_potter)
session.add(lord_of_the_rings)
session.add(maze_runner)
session.add(scorch_trials)

session.add(uwe_boll)
session.add(heinz_honzl)
session.add(josef_feff)

session.commit()
session.close()