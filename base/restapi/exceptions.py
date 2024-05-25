from rest_framework.exceptions import APIException


class TokenNotFound(APIException):
    status_code = 403
    default_detail = "Un Authenticate"
    default_code = "unauthorized"