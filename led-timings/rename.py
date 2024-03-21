"""A script for renaming sequential files of the form scope_<index>.csv to
the form: 200_rise.csv, 200_fall.csv, 400_rise.csv, ..., 1000_fall.csv.
"""

import os
import argparse
import re

def process_args():
    """Parse commandline args"""
    
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The path of files to rename')
    
    return parser

def get_num(s):
    """Extract the integer <i> in strings of form scope_<i>.csv"""
    
    pattern = "scope_([0-9]+).csv"
    
    m = re.match(pattern, s)
    
    return int(m[1])

if __name__ == '__main__':
    args = process_args().parse_args()
    
    csvs = os.listdir(args.path)
    
    assert(len(csvs) == 10)
    assert(not any('rise' in filename for filename in csvs))
    
    csvs.sort(key=get_num)
    print(csvs)
    
    i = 0
    
    for delay_us in [200, 400, 600, 800, 1000]:
        for measurement in ["rise", "fall"]:
            os.rename(os.path.join(args.path, csvs[i]),
                      os.path.join(args.path, f"{delay_us}_{measurement}.csv"))
            
            i += 1