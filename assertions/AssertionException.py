class AssertionException(Exception):

    def __init__(self, message):
        super().__init__("Assertion exception: {}".format(message))
