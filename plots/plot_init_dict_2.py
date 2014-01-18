# Plotting performance of init_dict_.py scripts
# mean values with variances as error bars

import matplotlib.pyplot as plt

x = [1, 2, 3]

y_1 = [0.6846,6.81236666666667,83.8166]
y_2 = [0.9993,9.55583333333333,113.167333333333]

y_1_err = [0.00000258999999999997,0.0322060233333333,1.19580806999999] 
y_2_err = [0.0000135100000000003,0.00176389333333333,1.10327929333334]

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
