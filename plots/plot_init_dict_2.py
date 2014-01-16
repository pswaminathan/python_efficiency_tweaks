# Plotting performance of init_dict_.py scripts
# mean values with variances as error bars

import matplotlib.pyplot as plt

x = [1, 2, 3]

y_1 = [0.691866666666667,6.48346666666667,110.885066666667]
y_2 = [0.935633333333333,9.11973333333333,142.784833333333]

y_1_err = [0.0000759633333333333,0.00322954333333333,4.70763596333331] 
y_2_err = [0.000147243333333332,0.0124217233333334,8.09982964333338]

x_labels = ["n = 10^6", "n = 10^7", "n = 10^8"]

plt.figure()
plt.errorbar(x, y_1, yerr=y_1_err, fmt='-x')
plt.errorbar(x, y_2, yerr=y_2_err, fmt='-^')

plt.xticks(x, x_labels)
plt.xlim([0,4])
plt.xlabel('size n')
plt.ylabel('cpu time in sec')
plt.yscale('log')
plt.title('Dictionary initialization 2')
plt.legend(['init_dict_3.py', 'init_dict_4.py'], loc='upper left')

#plt.show()
plt.savefig('PNGs/init_dict_2.png')
