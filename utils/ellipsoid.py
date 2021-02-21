import numpy as np
from scipy.linalg import lstsq
from numpy.linalg import eigh


def elipsoid(x, trial):
    #     a = x[0]
    #     b = x[1]
    #     c = x[2]
    #     x0 = x[3]
    #     y0 = x[4]
    #     x0 = y[5]
    return np.sum(np.square(np.sum(np.divide(np.square(trial.values + x[3:6]), np.square(x[0:3])), 1) - 1))


def calculate_ellipsoid_parameters(x, y, z):
    # This method is based on alghoritm from:
    # https://www.st.com/resource/en/design_tip/dm00286302-ellipsoid-or-sphere-fitting-for-sensor-calibration-stmicroelectronics.pdf
    D = np.array([x * x, y * y, z * z, 2 * x * y, 2 * x * z, 2 * y * z, 2 * x, 2 * y, 2 * z]).transpose()

    v, _, _, _ = lstsq(D.transpose().dot(D), D.transpose().dot(np.ones((len(x), 1))))

    A = np.array([[v[0, 0], v[3, 0], v[4, 0], v[6, 0]],
                  [v[3, 0], v[1, 0], v[5, 0], v[7, 0]],
                  [v[4, 0], v[5, 0], v[2, 0], v[8, 0]],
                  [v[6, 0], v[7, 0], v[8, 0], -1]])
    ofs, _, _, _ = lstsq(-1 * A[0:3, 0:3], v[6:9])

    Tmtx = np.eye(4)
    Tmtx[3, 0:3] = ofs.transpose()
    AT = Tmtx.dot(A.dot(Tmtx.transpose()))

    ev, rotM = eigh(AT[0:3, 0:3]/(-1*AT[3, 3]))
    gain = np.sqrt(np.ones(len(ev))/ev)

    return ofs, gain, rotM
