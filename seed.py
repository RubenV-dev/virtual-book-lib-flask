from app import app
from models.book import db, Book

books = [
    Book(
        title="The Hobbit",
        rating=5.0,
        genre="Fantasy",
        comment="A timeless adventure with unforgettable characters."
    ),
    Book(
        title="1984",
        rating=4.8,
        genre="Dystopian",
        comment="A chilling look at surveillance and authoritarianism."
    ),
    Book(
        title="To Kill a Mockingbird",
        rating=4.9,
        genre="Classic",
        comment="An emotional story about justice and compassion."
    ),
    Book(
        title="The Great Gatsby",
        rating=4.3,
        genre="Classic",
        comment="Beautifully written with themes of wealth and ambition."
    ),
    Book(
        title="Dune",
        rating=4.9,
        genre="Science Fiction",
        comment="Epic world-building and political intrigue."
    ),
    Book(
        title="The Catcher in the Rye",
        rating=4.0,
        genre="Coming of Age",
        comment="A classic novel with a memorable narrator."
    ),
    Book(
        title="The Alchemist",
        rating=4.5,
        genre="Adventure",
        comment="Inspirational story about following your dreams."
    ),
    Book(
        title="Harry Potter and the Sorcerer's Stone",
        rating=5.0,
        genre="Fantasy",
        comment="A magical beginning to an incredible series."
    ),
    Book(
        title="The Martian",
        rating=4.8,
        genre="Science Fiction",
        comment="Funny, suspenseful, and scientifically engaging."
    ),
    Book(
        title="Atomic Habits",
        rating=4.9,
        genre="Self Help",
        comment="Excellent advice on building good habits and breaking bad ones."
    )
]

def seed_books():
    db.drop_all()
    db.create_all()
    db.session.bulk_save_objects(books)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seed_books()
        print("✅ Database seeded!")