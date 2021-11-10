import time
from contextlib import contextmanager

class Timer():

    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f" It takes: {time.time()-self.start} seconds")
        return None


with Timer():
    a = 20_000_000
    for _ in range(a):
        pass


# bonus
@contextmanager
def timer():
    start = time.time()
    yield None
    print(f"It takes {time.time() - start} seconds")


with timer():
    a = 20_000_000
    for _ in range(a):
        pass

