# Plotting performance of init_dict_.py scripts
# mean values with variances as error bars

import matplotlib.pyplot as plt

x = [1, 2, 3]

y_1 = [0.471266666666667,4.79836666666667,50.8614]
y_2 = [0.2684,2.66703333333333,30.5070333333333]

y_1_err = [0.0000466533333333335,0.0126118533333334,0.0066612900000002] 
y_2_err = [0.00001677,0.00207020333333334,0.213477853333334]

x_labels = ["n = 10^6", "n = 10^7", "n = 10^8"]

plt.figure()
plt.errorbar(x, y_1, yerr=y_1_err, fmt='-x')
plt.errorbar(x, y_2, yerr=y_2_err, fmt='-^')

plt.xticks(x, x_labels)
plt.xlim([0,4])
plt.xlabel('size n')
plt.ylabel('cpu time in sec')
plt.yscale('log')
plt.title('Dictionary initialization 1')
plt.legend(['init_dict_1.py', 'init_dict_2.py'], loc='upper left')

#plt.show()
plt.savefig('PNGs/init_dict_1.png')
