import os
import argparse
import csv
import re

def process_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('path')
    
    return parser

def get_num(s):
    pattern = "scope_([0-9]+).csv"
    
    m = re.match(pattern, s)
    
    return int(m[1])

if __name__ == '__main__':
    args = process_args().parse_args()
    
    csvs = os.listdir(args.path)
    csvs.sort(key=get_num)
    
    print("Found csvs", csvs)
    
    assert(len(csvs) == 5)
    assert(not any('200' in filename for filename in csvs))
    
    i = 0
    
    for delay_us in [200, 400, 600, 800, 1000]:
        os.rename(os.path.join(args.path, csvs[i]),
                    os.path.join(args.path, f"{delay_us}.csv"))
        
        i += 1