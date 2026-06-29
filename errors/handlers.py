from flask import jsonify
from werkzeug.exceptions import HTTPException

from errors.exceptions import APIError


def register_error_handlers(app):

    @app.errorhandler(APIError)
    def handle_api_error(error):

        return jsonify({
            "success": False,
            "error": {
                "code": error.status_code,
                "message": error.message
            }
        }), error.status_code


    @app.errorhandler(HTTPException)
    def handle_http_exception(error):

        return jsonify({
            "success": False,
            "error": {
                "code": error.code,
                "message": error.description
            }
        }), error.code


    @app.errorhandler(Exception)
    def handle_unknown_error(error):

        print(error)

        return jsonify({
            "success": False,
            "error": {
                "code": 500,
                "message": "Internal Server Error"
            }
        }), 500