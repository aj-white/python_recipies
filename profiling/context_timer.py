from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter_ns()
    yield
    elapsed = time.perf_counter_ns()

    print(f"Code ran in {elapsed: 3f} ns")
