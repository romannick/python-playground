class APIException(Exception):
    status_code = 500
    detail = "An error occurred"

    def __init__(self, detail=None, status_code=None):
        if detail:
            self.detail = detail

        if status_code:
            self.status_code = status_code

        super().__init__(self.detail)


class NotFound(APIException):
    status_code = 404
    detail = "Resource not found"


class BadRequest(APIException):
    status_code = 400
    detail = "Bad request"