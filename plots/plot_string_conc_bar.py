# Plotting performance of string_conc_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [1,23.1484249097938]
variance = [0,3.27999930582225]
scripts = ['string_conc_1.py', 'string_conc_2.py']

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)

plt.ylabel('rel. performance gain')
plt.title('String concatenation - Speed improvements')

#plt.show()
plt.savefig('PNGs/string_conc_bar.png')
