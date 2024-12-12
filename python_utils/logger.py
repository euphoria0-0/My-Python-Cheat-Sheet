import os
import time
import logging


# logger
def create_logger(log_dir='logs'):
    start_time_str = time.strftime('%Y%m%d-%H%M%S', time.localtime()) 
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s] %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    file_handler = logging.FileHandler(os.path.join(log_dir, f"log_{start_time_str}.log"))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger