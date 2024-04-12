import torch
import sys
import argparse

import seaborn as sn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# Hello world code; plots a signal.
fs = 250
f = 5
T = 2


def pp(f, T, fs):
    """

    :param f: the frequency of a signal
    :param T: the length of the signal in seconds
    :param fs: the samplling rate
    :return: s: signal, t: time axis in seconds
    """

    t = np.linspace(0,T,fs)
    s = np.sin(2*np.pi*f*t)
    return s, t



if __name__ == "__main__":
    """
    A simple template code for a python project.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', dest='filename', help='output filename', type=str, required=False)
    args = parser.parse_args()

    # print version information of python and imported packages.
    print(f"Python version: {sys.version}")
    print(f"Pytorch version: {torch.__version__}")
    print(f"Numpy version: {np.__version__}")
    print(f"Seaborn version: {sn.__version__}")
    print(f"Pandas version: {pd.__version__}")
    print(f"Matplotlib version: {matplotlib.__version__}")
    # Generate signal and plot it
    s, t = pp(f,T,fs)
    plt.plot(t, s, 'o-')
    if args.filename:
        plt.savefig("python_template.png")
