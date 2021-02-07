import numpy as np


def elipsoid(x, trial):
    #     a = x[0]
    #     b = x[1]
    #     c = x[2]
    #     x0 = x[3]
    #     y0 = x[4]
    #     x0 = y[5]
    return np.sum(np.square(np.sum(np.divide(np.square(trial.values +
                                                       x[3:6]), np.square(x[0:3])), 1) - 1))