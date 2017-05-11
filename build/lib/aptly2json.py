import ast
import json
import re
from itertools import groupby

import sys


def parse_next_package(iter_lines):
    def safe_cast(val):
        try:
            return ast.literal_eval(val)
        except:
            return val.strip()
    parsed = {}

    for line in iter_lines:
        key,value = line.split(":",1)
        parsed[key] = safe_cast(value)
        if key == "Description":
            break
    else:
        raise StopIteration
    try:
        line = next(iter_lines)
    except StopIteration:
        line = None

    while line:
        parsed['Description'] += "\n"+line
        try:
            line = next(iter_lines)
        except StopIteration:
            break

    return parsed

def parse_packages_iter(iter_lines):
    while True:
        yield parse_next_package(iter_lines)



def get_sorted_rows_objects(package_iter):
    return sorted(parse_packages_iter(package_iter), key=lambda x: (x['Package'],map(int, re.findall("[0-9]+", x['Version']))), reverse=True)

def parse_packages(packages_txt):
    package_iter = iter(packages_txt.splitlines())
    data = {}
    packages_objects = get_sorted_rows_objects(package_iter)
    for package_name,versions in groupby(packages_objects,lambda x:x['Package']):
        data.setdefault('provides',set()).add(package_name)
        data.setdefault('data',{})[package_name]=list(versions)
    data['provides'] = list(data.get('provides',[]))
    return data


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="parse input from `aptly package show` into json",usage="\n `python -m aptly2json -f some_input.txt`\n  - or - \n`aptly package show \"(Version >=0)\" | python -m aptly2json -I`")
    grp = parser.add_mutually_exclusive_group()
    grp.add_argument("-I","--stdin",help="read package input from stdin",action='store_true',)
    grp.add_argument("-f","--infile",help="read package input from a specified file",type=file)
    args = parser.parse_args()
    if args.stdin is False and args.infile is None:
        parser.print_help(sys.stderr)
        parser.error('exactly one of `--stdin` or `--infile=<fname>` is required')
    elif args.stdin and not args.infile:
        args.infile = sys.stdin

    print json.dumps(parse_packages(args.infile.read()))

