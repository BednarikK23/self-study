import numpy as np
import matplotlib.pyplot as plt
# A plot is a graphical technique for representing a data set, usually as a
# graph showing the relationship between two or more variables


if __name__ == '__main__':
    # from -100 to 100 gimme 200 values evenly distributed
    x = np.linspace(-100, 100, 201)
    # or: x = np.arange(-100, 101, 1)

    y = 0.5 * x ** 2 + 2 * x
    z = np.sin(x) * 2000
    w = np.log(x) * 1000

    # 3rd parameter specifies the style of the line
    #   - 1st letter means color r -red, g - green, b - blue...
    #   - then you specify characters of the marks
    plt.plot(x, y, 'bo')  # takes x values and y values and plots the graph...
    plt.plot(x, z, 'r--')
    plt.plot(x, w, 'y^')

    plt.show()

