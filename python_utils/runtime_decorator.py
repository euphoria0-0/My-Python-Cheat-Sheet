import time

# decorator
class RunTime(object):
    def __init__(self, mode='Train'):
        self.mode = mode

    def __call__(self, func):
        def timeit_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f'{self.mode} Time (s): {total_time:.4f}')  # logger.info
            return result
        return timeit_wrapper