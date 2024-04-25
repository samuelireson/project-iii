import matplotlib.pyplot as plt
import numpy as np


def test():
    delta = 0.001
    xrange = np.arange(-1.1, 1.1, delta)
    yrange = np.arange(-1.1, 1.1, delta)
    x, y = np.meshgrid(xrange, yrange)

    equation = x**4 - x**2 + y**2

    plt.contour(x, y, equation, [0], colors=['black'], linewidths=[1])
    plt.axis("equal")
    plt.axis(False)
    plt.savefig('./affine-curve/lemniscate.pgf',
                transparent=True, bbox_inches=None)
    plt.show()


if __name__ == '__main__':
    test()
