# Plotting performance of string_subst_.py scripts
# bar chart of relative comparison with variances as error bars

import numpy as np
import matplotlib.pyplot as plt

performance = [1,0.096848237372566,0.994821055040085]
variance = [0,0.0000646513842611129,0.000302580396972356]
scripts = ['string_subst_1.py', 'string_subst_2.py', 'string_subst_3.py']

x_pos = np.arange(len(scripts))

plt.bar(x_pos, performance, yerr=variance, align='center', alpha=0.5)
plt.xticks(x_pos, scripts)
plt.ylim([0,4])

plt.ylabel('rel. performance gain')
plt.title('String substitution - Speed improvements')

#plt.show()
plt.savefig('PNGs/string_subst_bar.png')
