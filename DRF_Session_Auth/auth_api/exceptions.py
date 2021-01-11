from rest_framework.exceptions import APIException
from rest_framework import status

class Custom409(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'A conflict occurred'