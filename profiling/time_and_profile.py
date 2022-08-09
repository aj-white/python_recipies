"""Courtesy of Bob @ PyBites https://www.youtube.com/watch?v=nnkY3dcH74o"""

import cProfile
from functools import wraps
from pstats import Stats
from pstats import SortKey
from time import perf_counter


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
