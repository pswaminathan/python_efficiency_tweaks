# Dictionary initialization

import time
from max_size import n

orig_dict = {}

start_time = time.clock()

for i in range(0, n):
    try:
        orig_dict[i] += 1
    except KeyError:
        orig_dict[i] = 1
     
elapsed_time = time.clock() - start_time
print("Time elapsed: {0:.4f} sec".format(elapsed_time))
