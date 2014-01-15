# Plotting performance of string_subst_.py scripts
# mean values with variances as error bars

import matplotlib.pyplot as plt

x = [1, 2, 3]

y_1 = [0.0676,0.671266666666667,6.5625]
y_2 = [0.659833333333333,6.68196666666667,74.8843333333333]
y_3 = [0.0668333333333333,0.687233333333333,6.58736666666667]

y_1_err = [0.000000180000000000002,0.00000532333333333352,0.00000408999999999994] 
y_2_err = [0.00000758333333333342,0.00673880333333339,0.291411603333335]
y_3_err = [0.000000943333333333331,0.00109408333333333,0.00257057333333333]

x_labels = ["n = 10^6", "n = 10^7", "n = 10^8"]

plt.figure()
plt.errorbar(x, y_1, yerr=y_1_err, fmt='-x')
plt.errorbar(x, y_2, yerr=y_2_err, fmt='-^')
plt.errorbar(x, y_3, yerr=y_3_err, fmt='-o')

plt.xticks(x, x_labels)
plt.xlim([0,4])
plt.xlabel('size n')
plt.ylabel('cpu time in sec')
plt.yscale('log')
plt.title('String substitution')
plt.legend(['string_subst_1.py', 'string_subst_2.py', 'string_subst_3.py'], loc='upper left')

#plt.show()
plt.savefig('PNGs/string_subst.png')
