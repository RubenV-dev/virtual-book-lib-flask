class APIError(Exception):

    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code

        super().__init__(self.message)


class BookNotFound(APIError):

    def __init__(self):
        super().__init__(
            message="Book not found.",
            status_code=404
        )