# Plotting performance of init_dict_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [1,1.74072653463125,0.626643645624977]
variance = [0,0.00452313458473456,0.022025881015751]
scripts = ['init_dict_1.py', 'init_dict_2.py', 'init_dict_3.py']

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
plt.ylim([0,4])

plt.ylabel('rel. performance gain')
plt.title('Dictionary initialization - Speed improvements')

#plt.show()
plt.savefig('PNGs/init_dict_bar.png')
