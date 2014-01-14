# List modification

import time
from max_size import n

orig_list = ["abc" for i in range(1, n)]

start_time = time.clock()

new_list = [len(string) for string in orig_list]

elapsed_time = time.clock() - start_time
print ("Time elapsed: {0:.4f} sec".format(elapsed_time))

