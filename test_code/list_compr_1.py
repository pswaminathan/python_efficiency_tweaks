# List initiation

import time
from max_size import n

start_time = time.clock()

even_nums = []
for i in range(1, n):
    if i % 2 == 0:
        even_nums.append(i)

elapsed_time = time.clock() - start_time
print ("Time elapsed: {0:.4f} sec".format(elapsed_time))


