import functools
import time


def timer(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))
        return result

    return wrapper