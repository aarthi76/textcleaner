class TextCleanerError(Exception):
    """Base class for exceptions in this module."""
    pass

class EmptyTextError(TextCleanerError):
    """Raised when the input text is empty."""

    def __init__(self, message="Input text cannot be empty."):
        self.message = message
        super().__init__(self.message)