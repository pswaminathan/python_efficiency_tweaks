# Plotting performance of init_dict_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [1,0.742326411677032]
variance = [0,0.00108399990572723]
scripts = ['init_dict_1.py', 'init_dict_2.py']

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
plt.ylim([0,2])

plt.ylabel('rel. performance gain')
plt.title('Dictionary initialization 2 - Speed improvements')

#plt.show()
plt.savefig('PNGs/init_dict_bar_2.png')
