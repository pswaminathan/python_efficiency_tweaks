# Plotting performance of list_compr_.py scripts
# mean values with variances as error bars

import matplotlib.pyplot as plt

x = [1, 2, 3]

y_1 = [0.311333333333333,3.1579,31.6033]
y_2 = [0.199333333333333,1.9834,20.1541333333333]
y_3 = [0.356533333333333,3.5213,35.5170333333333]

y_1_err = [0.00000880333333333338,0.01635529,0.26173053] 
y_2_err = [0.000000863333333333338,0.000042249999999999,0.000124843333333347]
y_3_err = [0.000000303333333333337,0.0000198699999999986,0.00339490333333345]

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
plt.title('List item if-condition')
plt.legend(['list_compr_1.py', 'list_compr_2.py', 'list_compr_3.py'], loc='upper left')

#plt.show()
plt.savefig('PNGs/list_compr.png')
