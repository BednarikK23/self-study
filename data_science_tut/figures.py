import numpy as np
import matplotlib.pyplot as plt

# moving from subplots -> subplots were in one figure but if we wanna have more
# figures we have to do this..:

if __name__ == '__main__':
    x = np.arange(0, 101, 0.2)
    y1 = np.sin(x)
    y2 = x ** 2 + 2 * x
    y3 = np.log(x)

    plt.figure()
    ax1 = plt.subplot(211)
    ax1.plot(x, y1, 'g')

    ax2 = plt.subplot(212)
    ax2.plot(x, y2, 'r--')

    plt.figure(2)
    plt.plot(x, y1)

    plt.figure(3)
    plt.plot(x, y3)

    plt.show()
