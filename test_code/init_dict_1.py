# Dictionary initialization

import time
from max_size import n

orig_dict = {l:0 for l in 'a,b,c,d'.split(',')}

start_time = time.clock()

for i in range(0, n):
    char = 'abcd'[i%4]
    if char not in orig_dict:
        orig_dict[char] = 0
    orig_dict[char] += 1

elapsed_time = time.clock() - start_time
print ("Time elapsed: {0:.4f} sec".format(elapsed_time))

