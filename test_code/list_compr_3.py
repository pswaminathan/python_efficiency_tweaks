# List initiation

import time
from max_size import n

start_time = time.clock()

even_nums = list(filter((lambda x: x % 2 != 0), range(1, n)))

elapsed_time = time.clock() - start_time
print ("Time elapsed: {0:.4f} sec".format(elapsed_time))


