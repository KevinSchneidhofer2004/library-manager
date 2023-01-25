from sqlalchemy import Column, String, Integer, ForeignKey

from sqlalchemy.orm import relationship

from base import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    book = relationship("Book", backref = "customers")

    def __init__(self, name):
        self.name = name