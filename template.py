#!/usr/bin/env python3
import functools
import itertools
import re
import time
from collections import Counter, defaultdict
from io import StringIO

import numpy as np

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable=None, **kwargs):
        return iterable

# sys.path.append(os.path.dirname(__file__))
# from common_patterns import Point2D


def part1(parsed):
    pass

def part2(parsed):
    pass

def parse_input(data_src):
    data_src.seek(0)
    for line in data_src:
        pass
    return parsed

def main():
    test_data, test_answers = get_test_data()
    with open(__file__[:-3] + '-input.dat') as infile:
        assert part1(parse_input(test_data)) == test_answers[0]
        print_result('1', part1, parse_input(infile))  # -

        assert part2(parse_input(test_data)) == test_answers[1]
        print_result('2', part2, parse_input(infile))  # -

def print_result(part_label, part_fn, *args):
    start = time.perf_counter()
    result = part_fn(*args)
    end = time.perf_counter()
    print(f"Part {part_label}: {result}  ({int((end-start)*1000)} ms)")

def get_test_data():
    """Keep test data out of the way at the bottom of this file."""
    TEST_INPUT = """
test data
"""
    TEST_RESULTS = (0, 0)

    return StringIO(TEST_INPUT.strip()), TEST_RESULTS

if __name__ == '__main__':
    main()
