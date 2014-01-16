# Plotting performance of list_compr_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [1.1280326252671,1.7754282999013,1]
variance = [0.000239773282772946,0.000173691707594337,0]
scripts = ['list_compr_1.py', 'list_compr_2.py', 'list_compr_3.py']

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
plt.axhline(y=1, linestyle='--', color='black')
plt.ylim([0,4])

plt.ylabel('rel. performance gain')
plt.title('List item if-condition - Speed improvements')

#plt.show()
plt.savefig('PNGs/list_compr_bar.png')
