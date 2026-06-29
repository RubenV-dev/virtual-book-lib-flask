
from flask import Flask
from config import Config
from models.book import db
from routes.book_routes import book_bp
from errors.handlers import register_error_handlers

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

register_error_handlers(app)

with app.app_context():
    db.create_all()

app.register_blueprint(book_bp, url_prefix="/api")

@app.route("/")
def home():
    return {
        "message": "Book Store API Running!"
    }

if __name__ == "__main__":
    app.run(debug=True)