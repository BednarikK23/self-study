import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.arange(0, 101, 0.2)
    y1 = np.sin(x)
    y2 = x ** 2 + 2 * x

    # 2 functions - want to have them in separate plot but same window, use:
    # first digit of subplot tells us how many rows this window gonna have
    # second digit effects the columns of subplots
    # last digit is index of this particular subplot
    ax1 = plt.subplot(221)
    ax2 = plt.subplot(222)
    ax3 = plt.subplot(223)
    ax4 = plt.subplot(224)

    ax1.plot(x, y1)
    ax2.plot(x, y2)
    ax3.plot(x, x, "go")
    ax4.plot(x, y2, "r--")

    # for better layout:
    plt.tight_layout()
    plt.show()

