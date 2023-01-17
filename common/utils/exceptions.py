from common.utils import status_codes


class ParamsIsNullException(Exception):

    def __init__(self, message):
        self.status = status_codes.STATUS_PARAMS_ERROR
        self.message = status_codes.MESSAGE_PARAMS_ERROR % message
        super(ParamsIsNullException, self).__init__(message)

class GenericError(Exception):

    def __init__(self, status, message):
        self.status = status
        self.message = message
        super(GenericError, self).__init__(message)