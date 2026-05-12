from fastapi.exceptions import HTTPException

class NotFoundException(HTTPException):
    def __init__(self, status_code = 404, detail = 'data not found', headers = None):
        super().__init__(status_code, detail, headers)