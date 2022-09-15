"""Courtesy of Bob @ PyBites https://www.youtube.com/watch?v=nnkY3dcH74o"""

import cProfile
import time

from functools import wraps
from pstats import Stats
from pstats import SortKey

import logging

logging.basicConfig(
    filename="profile.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s %(message)s",
)

def time_logger(file: str):
  """Logs profile times, enables adding labels for clearer logs when profiling methods"""
    def timing(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"Elapsed time {func.__name__}: {end - start} seconds")
            elapsed = end - start
            logging.info("%s - %s took %s seconds", file, func.__name__, elapsed)
            return result

        return wrapper

    return timing




def timing(func):
  """A Simple timing decorator"""
  @wraps(func)
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    print(f"Elapsed time {func.__name__}: {end - start} seconds")
    return result
  return wrapper


def profile(func):
  """A simple profiling decorator"""
  @wraps(func)
  def wrapper(*args, **kwargs):
    with cProfile.Profile() as pr:
      result = func(*args, **kwargs)
    ps = Stats(pr)
    print("Most time spent in general:")
    ps.sort_stats(SortKey.CUMULATIVE).print_stats(10)
    print("Functions taking most time:")
    ps.sort_stats(SortKey.TIME).print_stats(10)
    return result
  return wrapper
