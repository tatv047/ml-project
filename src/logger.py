import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # format of the log message 
    level=logging.INFO
)

"""For testing only"""

# if __name__ == "__main__":
#     # logging.info("This is an info message")
#     logging.warning("This is a warning message")
#     # logging.error("This is an error message")
#     # logging.critical("This is a critical message")
#     # logging.debug("This is a debug message")
#     # logging.exception("This is an exception message")