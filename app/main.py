#!/usr/bin/env python
"""
author: Lukasz Dynowski
email: ludd@bioinforamtics.dtu.dk
license: MIT
"""
import os
import json
import time
import argparse
from src.statistics import Statistic


parser = argparse.ArgumentParser(description="Program counts codons found in a fsa file.")
parser.add_argument("-f", "--file_path", default=None, help="path to fsa file")
parser.add_argument("-o", "--output_path", default=None, help="program's output path")

args = parser.parse_args()

DATA_FILE = None
FILE_PATH = args.file_path
OUTPUT_PATH = args.output_path

try:
    assert os.path.exists(FILE_PATH), "Requested file does not exist."
    assert FILE_PATH.endswith('fsa'), "Requested file is not a fsa file."
    if OUTPUT_PATH is not None:
        assert os.path.exists(OUTPUT_PATH), "Output path does not exist."

    DATA_FILE = open(FILE_PATH)
    content = DATA_FILE.read()

    assert content != "", "Requested file is empty."
    assert content[0] == ">", "Requested file is not valid fsa file."
except AssertionError as err:
    print("Error:", err.message)
    exit()

stats = Statistic(DATA_FILE)

results = stats.count_nucleotides()

data = json.dumps(results)
if OUTPUT_PATH:
    OUTPUT_PATH = OUTPUT_PATH + "output.json"
    with open(OUTPUT_PATH, 'w') as output_file:
        output_file.write(data)
        print("Data was saved at: " + OUTPUT_PATH)
else:
    print(data)
