#!/usr/bin/env python3

import argparse
import json
import os
import sys
import time
from statistics import Statistic

parser = argparse.ArgumentParser(description="Program counts nucleotides found in FASTA file.")
parser.add_argument("-i", "--input-file", type=argparse.FileType('r'), nargs='+', default=None, help="Path to FASTA file(s). If more than one file is provided then use space as separator.")
parser.add_argument("-o", "--output-dir", default=None, help="Path to output directory.")
args = parser.parse_args()


def quit(status_code, err):
    print(err)
    exit(status_code)


def validate_file(file):
    try:
        header = file.readline()
        content = file.readline()
        fname = file.name.strip('/')[-1]
        assert header != "", f"File '{fname}' is empty."
        assert header[0] == ">", f"File '{fname}' isn't a FASTA file."
        assert content != "", f"File '{fname}' has no content."
    except AssertionError as err:
        quit(1, err)


if args.output_dir is None and args.input_file is None:
    parser.print_help()

if args.output_dir:
    try:
        assert args.output_dir.startswith('/'),  f"Output directory '{args.output_dir}' MUST starts with absolute path."

        os.makedirs(args.output_dir, exist_ok=True)
    except AssertionError as err:
        quit(1, err)
    except PermissionError as err:
        quit(1, err)


if args.input_file:
    for file in args.input_file:
        validate_file(file)

    results = {}
    for file in args.input_file:
        count = Statistic(file.name).count_nucleotides()
        results.update(count)

    json_data = json.dumps(results)
    if args.output_dir:
        with open(f'{args.output_dir}/results.json', 'w') as of:
            of.write(json_data)
    else:
        print(json_data)
