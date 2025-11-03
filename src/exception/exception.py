import sys

class CustomException(Exception):
    """A custom exception class that extends the built-in Exception class."""

    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message
        _,_, exe_tb = error_detail.exc_info()

        self.lineno = exe_tb.tb_lineno
        self.filename = exe_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script: {self.filename} at line number: {self.lineno} with message: {self.error_message}"


