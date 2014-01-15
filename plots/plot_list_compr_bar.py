# Plotting performance of list_compr_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [1,1.5740394021841,0.886609991697391]
variance = [0,0.000256035145228169,0.000146620074732823]
scripts = ['list_compr_1.py', 'list_compr_2.py', 'list_compr_3.py']

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
plt.ylim([0,4])

plt.ylabel('rel. performance gain')
plt.title('List item if-condition - Speed improvements')

#plt.show()
plt.savefig('PNGs/list_compr_bar.png')
