####################################################################
# List of 2D-coordinates for the centres of normally distributed clusters of points with the same label
CLUSTER_CENTRES = [(0,0),(1,1)]  # <-- cluster of "zeros" around (0,0), cluster of "ones" around (1,1)

# Corresponding list containing the standard deviation (of dist. from centre) of the points in each cluster
CLUSTER_STDDEVS = [0.5, 0.5]

# Total number of points in each cluster
CLUSTER_SIZE = 500

# Directory in which to save the data (WILL BE ERASED FIRST!)
DIR = 'bigcluster_raw'

# Number of files to create for each cluster
FILES_PER_CLUSTER = 7
####################################################################

import os
import numpy as np
import tensorflow as tf

# Delete previously generated data if there are any, and create fresh directory
try:
    tf.gfile.DeleteRecursively(DIR)
except tf.OpError:
    pass
os.makedirs(DIR)

# Create a cluster for each cluster centre
num_clusters = len(CLUSTER_CENTRES)
for i in range(num_clusters):

    points = CLUSTER_STDDEVS[i] * np.random.randn(CLUSTER_SIZE, 2) + CLUSTER_CENTRES[i]
    
    # Break the cluster into files and write them
    a = 0
    max_lines_per_file = int(np.ceil(CLUSTER_SIZE / FILES_PER_CLUSTER))
    labels = (i * np.ones(CLUSTER_SIZE))[:,None]
    for j in range(FILES_PER_CLUSTER):
        b = min(CLUSTER_SIZE, a + max_lines_per_file)
        file_contents = np.concatenate((points[a:b,:], labels[:b-a,:]), axis=-1)

        # Write a file 
        filename = os.path.join(DIR, (str(i) + "_" + str(j) + ".csv"))
        print("Writing %s" % filename)
        np.savetxt(fname=filename, X=file_contents, fmt="%g", delimiter=",")
        a = b
