from book import Book
from base import Session, engine, Base
from customer import Customer

Base.metadata.create_all(engine)

session = Session()

harry_potter = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Bloomsburry Publishing", 1995, True)
lord_of_the_rings = Book("Lord Of The Rings", "J.R.R. Tolkien", "Allen & Unwin", 1935, True)
maze_runner = Book("The Maze Runner", "James Dashner", "Delacorte Press", 2009, True)
scorch_trials = Book("The Scorch Trials", "James Dashner", "Delacorte Press", 2010, True)

uwe_boll = Customer("Uwe Boll", harry_potter)
heinz_honzl = Customer("Heinz Honzl", lord_of_the_rings)
josef_feff = Customer("Josef Feff", scorch_trials)

session.add(harry_potter)
session.add(lord_of_the_rings)
session.add(maze_runner)
session.add(scorch_trials)

session.add(uwe_boll)
session.add(heinz_honzl)
session.add(josef_feff)

session.commit()
session.close()