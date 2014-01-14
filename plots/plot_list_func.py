# Plotting performance of list_func_.py scripts
# mean values with variances as error bars

import matplotlib.pyplot as plt

x = [1, 2, 3]

y_1 = [0.2971,2.98643333333333,30.7357666666667]
y_2 = [0.131166666666667,1.27486666666667,13.0668333333333]
y_3 = [0.0866666666666667,0.884266666666667,8.6227]

y_1_err = [0.0000247899999999999,0.00660144333333333,0.395627923333333] 
y_2_err = [0.0000133433333333333,0.00684884333333334,0.475046083333333]
y_3_err = [0.0000000133333333333341,0.000115423333333333,0.00209821000000001]

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
plt.title('Lists item function call')
plt.legend(['list_func_1.py', 'list_func_2.py', 'list_func_3.py'], loc='upper left')

#plt.show()
plt.savefig('list_func.png')
