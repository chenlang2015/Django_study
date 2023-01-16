from common.utils import status_codes


class ParamsIsNullException(Exception):

    def __init__(self, message):
        self.code = 403
        self.message = status_codes.MESSAGE_PARAMS_INVALID%message
        super(ParamsIsNullException, self).__init__(message)