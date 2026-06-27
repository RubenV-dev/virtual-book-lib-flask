from flask import Blueprint, request, jsonify
from models.book import Book, db

book_bp = Blueprint("books", __name__)

# GET ALL BOOKS
@book_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])


# GET SINGLE BOOK
@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())


# CREATE BOOK
@book_bp.route("/books", methods=["POST"])
def add_book():

    data = request.json

    book = Book(
        title=data["title"],
        genre=data["genre"],
        rating=data["rating"],
        comment=data["comment"]
    )

    db.session.add(book)
    db.session.commit()

    return jsonify(book.to_dict()), 201


# UPDATE BOOK
@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):

    book = Book.query.get_or_404(id)
    data = request.json

    book.title = data.get("name", book.title)
    book.genre = data.get("genre", book.genre)
    book.rating = data.get("rating", book.rating)
    book.comment = data.get("comment", book.comment)

    db.session.commit()

    return jsonify(book.to_dict())


# DELETE BOOK
@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):

    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    return jsonify({
        "message": "Book deleted successfully."
    })