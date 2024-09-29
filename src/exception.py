import sys
import logging

def error_message_detail(error, error_detail: sys) -> str:
    """
    Provides detailed error messages with filename, line number, and error description.
    
    Args:
        error: The original exception raised.
        error_detail: The sys module to extract exception details.
    
    Returns:
        A formatted string containing detailed error information.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script '{file_name}' on line {line_number}: {str(error)}"
    
    return error_message

# Custom exception handling class
class CustomException(Exception):
    """
    A custom exception class that logs and formats detailed error messages.
    """

    def __init__(self, error_message, error_detail: sys = None):
        """
        Initializes the CustomException instance.
        
        Args:
            error_message: The custom error message or exception raised.
            error_detail: Optional, the sys module to extract detailed error information.
        """
        super().__init__(error_message)
        self.error_message = error_message

        if error_detail is not None:
            self.error_message = error_message_detail(error=error_message, error_detail=error_detail)
        
        # Logs the error message automatically
        logging.error(self.error_message)

    def __str__(self) -> str:
        """
        String representation of the custom exception.
        
        Returns:
            The detailed error message as a string.
        """
        return self.error_message

