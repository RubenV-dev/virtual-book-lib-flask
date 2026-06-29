from flask import Blueprint, request, jsonify
from models.book import Book, db
from errors.exceptions import APIError, BookNotFound

book_bp = Blueprint("books", __name__)

# GET ALL BOOKS
@book_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify({ "success": True, "count": len(books), "data": [book.to_dict() for book in books] })


# GET SINGLE BOOK
@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        raise BookNotFound()
    return jsonify({ "success": True, "data": book.to_dict() })


# CREATE BOOK
@book_bp.route("/books", methods=["POST"])
def add_book():

    required_fields = ["title", "genre", "rating", "comment"]

    data = request.json

    # Adding some request validation
    if not data:
        raise APIError(message="Request body must be JSON.", status_code=400)
    
    for field in required_fields:
        if field not in data:
            raise APIError(message=f"Field '{field}' is required.", status_code=400)

    book = Book(
        title=data["title"],
        genre=data["genre"],
        rating=data["rating"],
        comment=data["comment"]
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({ "success": True, "data": book.to_dict() }), 201


# UPDATE BOOK
@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):

    book = Book.query.get(id)
    if not book:
        raise BookNotFound()
    data = request.json

    book.title = data.get("name", book.title)
    book.genre = data.get("genre", book.genre)
    book.rating = data.get("rating", book.rating)
    book.comment = data.get("comment", book.comment)

    db.session.commit()

    return jsonify({ "success": True, "data": book.to_dict() })


# DELETE BOOK
@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):

    book = Book.query.get(id)
    if not book:
        raise BookNotFound()

    db.session.delete(book)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Book deleted successfully."
    })