# String concatenation

import time
from max_size import n

letters = ['a' for i in range(1, n)]

start_time = time.clock()

my_str = ""
for letter in letters:
    my_str += letter

elapsed_time = time.clock() - start_time
print ("Time elapsed: {0:.4f} sec".format(elapsed_time))

