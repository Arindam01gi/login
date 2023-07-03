class MandatoryInputMissingException(Exception):
    def __init___(self, message):
        super(MandatoryInputMissingException, self).__init__(message)
        self.message = message

class PasswordLengthError(Exception):
    def __init___(self, message):
        super(PasswordLengthError, self).__init__(message)
        self.message = message