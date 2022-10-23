import numpy as np


def regression_function(x):
    pow5 = -2 * 10 ** -8 * x ** 5;
    pow4 = 6 * 10 ** -5 * x ** 4
    pow3 = -0.0561 * x ** 3
    pow2 = 27.739 * x ** 2
    pow1 = -6856.3 * x
    pow0 = 677754
    return pow5 + pow4 + pow3 + pow2 + pow1 + pow0

def new_regression(array, x):
    i=5
    result = 0
    for element in array:
        result+=element * x**i
        i-=1
    return result

if __name__ == '__main__':
    value_list = [561, 560, 526, 484, 466, 455, 441, 436, 430, 424, 418]
    value_array = np.array(value_list)

    percentage_list = [0, 7.69, 15.38, 18.46, 23.08, 30.77, 38.46, 46.15, 61.54, 76.92, 92.31]
    percentage_array = np.array(percentage_list)

    polyfit = np.polyfit(value_array, percentage_array, 5)



    print(new_regression(polyfit, 550))