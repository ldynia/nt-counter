#!/usr/bin/env python3

import argparse
import json
import os
import time
import sys
from statistics import Statistic

parser = argparse.ArgumentParser(description="Program counts nucleotides found in FASTA file.")
parser.add_argument("-i", "--input-file", type=argparse.FileType('r'), nargs='+', default=None, help="Path to FASTA file(s). If more than one file is provided then use space as separator.")
parser.add_argument("-o", "--output-dir", default=None, help="Path to output directory.")

args = parser.parse_args()


def quit(status_code, err):
    print(err)
    exit(status_code)


if args.output_dir:
    try:
        os.makedirs(args.output_dir, exist_ok=True)
    except PermissionError as e:
        quit(1, e)

try:
    assert os.path.exists(FILE_PATH), "Requested file does not exist."
    assert FILE_PATH.endswith('fsa'), "Requested file is not a fsa file."

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
if OUTPUT_DIR:
    output_file = OUTPUT_DIR + "/output.json"
    with open(output_file, 'w') as of:
        of.write(data)
        print("Data was saved at: " + OUTPUT_DIR)
else:
    print(data)
