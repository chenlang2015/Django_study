from rest_framework.response import Response

from common.utils import status_codes, constants


def response_response(status, message=None, result=None):
    return Response({
        constants.STATUS: status,
        constants.MESSAGE: message,
        constants.RESULT: result,
        constants.MODULE: constants.MODULE_NAME,
    })


def response_success(result=None):
    return response_response(
        status_codes.STATUS_SUCCESS,
        status_codes.MESSAGE_SUCCESS,
        result
    )