import matplotlib.pyplot as plt
import numpy as np

def tesk1(limit, Numberofptr):
    n = np.linspace(0, limit, Numberofptr)
    f_1 = pow(2, 10)*n + pow(2, 10)
    f_2 = pow(n, 3.5) -1000
    f_3 = 100*pow(n, 2.1) + 50

    plt.plot(n, f_1, color='red')
    plt.plot(n, f_2, color='blue')
    plt.plot(n, f_3, color='green')
    plt.show()

tesk1(5, 100)
tesk1(15, 300)
tesk1(50, 1000)