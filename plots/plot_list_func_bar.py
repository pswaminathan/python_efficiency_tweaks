# Plotting performance of list_func_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [1,2.31993328105027,3.45663135602093]
variance = [0,0.00228182736026489,0.00937418320073582]
scripts = ['list_func_1.py', 'list_func_2.py', 'list_func_3.py']

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
plt.ylim([0,4])

plt.ylabel('rel. performance gain')
plt.title('Lists item function call - Speed improvements')

#plt.show()
plt.savefig(‘./PNGs/list_func_bar.png')
