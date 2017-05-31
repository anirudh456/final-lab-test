
class AppException(Exception):
    lm = None

    def __init__(self, **litmap):
        self.lm = {'type': 'AppException', 'data': litmap}

    def __str__(self):
        return repr(self.lm)

    # to_client : AppException -> Litmap
    def to_client(self):
        return self.lm
