from flask import Flask, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isbn = db.Column(db.Integer)


def json(self):
    return {'name': self.name, 'price': self.price, 'isbn': self.isbn}


def add_Book(_name, _price, _isbn):
    new_book = Books(name=_name, price=_price, isbn=_isbn)
    db.session.add(new_book)
    db.session.commit()


def get_all_book():
    return [json(book) for book in Books.query.all()]


def get_Book(_isbn):
    return json(Books.query.filter_by(isbn = _isbn).first())


# delete book by isbn
def delete_book(_isbn):
    is_sucess =  Books.query.filter_by(isbn=_isbn).delete()
    db.session.commit()
    return bool(is_sucess)


def book_update_price(_isbn, _price):
    book_to_update = Books.query.filter_by(isbn=_isbn).first()
    book_to_update.price = _price
    db.session.commit()


def book_update_name(_isbn, _name):
    book_to_update = Books.query.filter_by(isbn=_isbn).first()
    book_to_update.name = _name
    db.session.commit()


def book_replace(_isbn, _name, _price):
    book_to_replace = Books.query.filter_by(isbn=_isbn).first()
    book_to_replace.name = _name
    book_to_replace.price = _price
    db.session.commit()


def __repr__(self):
    book_object = {
        'name': self.name,
        'price': self.price,
        'isbn': self.isbn
    }
    return json.dumps(book_object)
