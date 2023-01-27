from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_name = Column(String)
    publisher_name = Column(String)
    release_year = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    def __init__(self, title, author_name, publisher_name, release_year):
        self.title = title
        self.author_name = author_name
        self.publisher_name = publisher_name
        self.release_year = release_year
