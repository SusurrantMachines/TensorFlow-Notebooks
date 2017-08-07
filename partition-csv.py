SOURCE_DIR = 'bigcluster_raw'
TARGET_DIR = 'bigcluster_parted'
EXAMPLES_PER_FILE = 7

# List of subdirectories and the proportion of the total data allocated to each one
SUBSET_PROPORTIONS = {'train': 0.6, 'validation': 0.2, 'test':0.2}

# For K-fold cross validation, do this instead:
# K = ...
# SUBSET_NAMES = list(range(K)).append('test')
# SUBSET_PROPORTIONS = (K+1) * [1/(K+1)]  

######################

import random
import os
import numpy as np

# Get list of input filenames to be put in the blender
input_csv_file_list = [os.path.join(SOURCE_DIR, x) for x in os.listdir(SOURCE_DIR) if x.endswith('.csv')]

# Make a big list of all the lines in all the files and scramble it up
all_the_lines = []
for filename in input_csv_file_list:
    fid = open(filename, "r")    
    all_the_lines += fid.readlines()
    fid.close()    
random.shuffle(all_the_lines)

# For each subdirectory, find the block in 'all_the_lines' that that will be written to it.
# [This would look nicer done with list comprehensions, but we need to do everything in-place.]
subset_start = 0
n_lines = len(all_the_lines)
for subset in SUBSET_PROPORTIONS.keys():
    
    subset_dir = os.path.join(TARGET_DIR, subset)
    os.makedirs(subset_dir)
    
    subset_len = int(SUBSET_PROPORTIONS[subset] * n_lines)
    subset_end = subset_start + subset_len
    num_files_in_subset = int(np.ceil(subset_len / EXAMPLES_PER_FILE))
    
    # For each output file to be written in this subdirectory
    a = subset_start
    for i in range(num_files_in_subset):
        b = min(subset_end, a + EXAMPLES_PER_FILE)
        file_path = os.path.join(subset_dir, str(i) + '.csv')
        lines = all_the_lines[a:b]
        fid = open(file_path, "w")
        fid.writelines(lines)
        fid.close()
        a = b
