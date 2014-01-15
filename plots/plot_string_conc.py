# Plotting performance of string_conc_.py scripts
# mean values with variances as error bars

import matplotlib.pyplot as plt

x = [1, 2, 3]

y_1 = [0.384533333333333,4.27873333333333,40.8970666666667]
y_2 = [0.0181666666666667,0.1731,1.73586666666667]

y_1_err = [0.000105083333333334,0.0595094033333333,0.520736213333332] 
y_2_err = [0.000000423333333333333,0.0000000100000000000006,0.0000637733333333347]

x_labels = ["n = 10^6", "n = 10^7", "n = 10^8"]

plt.figure()
plt.errorbar(x, y_1, yerr=y_1_err, fmt='-x')
plt.errorbar(x, y_2, yerr=y_2_err, fmt='-^')

plt.xticks(x, x_labels)
plt.xlim([0,4])
plt.xlabel('size n')
plt.ylabel('cpu time in sec')
plt.yscale('log')
plt.title('String concatenation')
plt.legend(['string_conc_1.py', 'string_conc_2.py'], loc='upper left')

#plt.show()
plt.savefig('PNGs/string_conc.png')
