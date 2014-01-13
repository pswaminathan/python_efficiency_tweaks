# String substitution

import time
from max_size import n


start_time = time.clock()

strings = ['a' + '1' + '2' for i in range(1, n)]

elapsed_time = time.clock() - start_time
print ("Time elapsed: {0:.4f} sec".format(elapsed_time))

