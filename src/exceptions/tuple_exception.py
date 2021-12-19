class TupleException(Exception):
    def __init__(self, message):
        self.message = message
        super(TupleException, self).__init__(message)
