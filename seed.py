from app import app
from models.book import db, Book

books = [
    Book(
        title="The Hobbit",
        rating=5.0,
        genre="Fantasy",
        comment="A timeless adventure with unforgettable characters.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
    ),
    Book(
        title="1984",
        rating=4.8,
        genre="Dystopian",
        comment="A chilling look at surveillance and authoritarianism.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
    ),
    Book(
        title="To Kill a Mockingbird",
        rating=4.9,
        genre="Classic",
        comment="An emotional story about justice and compassion.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
    ),
    Book(
        title="The Great Gatsby",
        rating=4.3,
        genre="Classic",
        comment="Beautifully written with themes of wealth and ambition.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
    ),
    Book(
        title="Dune",
        rating=4.9,
        genre="Science Fiction",
        comment="Epic world-building and political intrigue.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
    ),
    Book(
        title="The Catcher in the Rye",
        rating=4.0,
        genre="Coming of Age",
        comment="A classic novel with a memorable narrator.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
    ),
    Book(
        title="The Alchemist",
        rating=4.5,
        genre="Adventure",
        comment="Inspirational story about following your dreams.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
    ),
    Book(
        title="Harry Potter and the Sorcerer's Stone",
        rating=5.0,
        genre="Fantasy",
        comment="A magical beginning to an incredible series.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
    ),
    Book(
        title="The Martian",
        rating=4.8,
        genre="Science Fiction",
        comment="Funny, suspenseful, and scientifically engaging.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
    ),
    Book(
        title="Atomic Habits",
        rating=4.9,
        genre="Self Help",
        comment="Excellent advice on building good habits and breaking bad ones.",
        img_url="https://images-na.ssl-images-amazon.com/images/I/91b0C2YNSrL.jpg"
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