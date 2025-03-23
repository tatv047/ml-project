import sys
import logging  
from src.logger import logging


def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    """
    exc_tb will return the traceback object which will have the information about the error.
    Like in which file the error occured, on which line the error occured, etc.
    """
    error_message = "Error occurred in python script name [{0}],line number [{1}], error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)
        

    def __str__(self):
        return self.error_message
    
# """Only for testing"""
# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.error(CustomException(e,sys))
        




















"""
The `os` module provides a portable way to use operating system-dependent functionality like reading or writing to the file system,
manipulating paths, processes, and environment variables.

Key features:
- File and directory operations (`os.path`, `os.mkdir`, `os.remove`)
- Process management (`os.system`, `os.fork`, `os.exec*`)
- Environment variables (`os.environ`)
- Platform-independent path handling (`os.path.join`, `os.path.split`)

The `sys` module provides access to Python interpreter variables and functions that interact with the interpreter.

Key features:
- Command-line arguments (`sys.argv`)
- Standard input/output/error streams (`sys.stdin`, `sys.stdout`, `sys.stderr`)
- Interpreter settings (`sys.path`, `sys.version`)
- Program termination (`sys.exit`)

Why These Modules Are Used

1. Portability: They abstract operating system differences, making your code work across Windows, macOS, Linux, etc.

2. System Integration: They allow Python programs to interact with the system environment, files, processes.

3. Interpreter Control: `sys` specifically lets you control Python's runtime behavior.

4. Command-line Applications: They're essential for building CLI tools that need to process arguments, read/write files, 
and interact with the environment.

These modules are fundamental for any Python program that needs to interact with the underlying operating system or control 
aspects of the Python interpreter itself.
"""
