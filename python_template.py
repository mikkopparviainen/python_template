import torch
import sys

import seaborn as sn
import seaborn
import pandas as pd
import pandas
import numpy as np
import numpy
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

import types
# Find out what modules are imported
def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__


if __name__ == "__main__":
    # print version information of python and imported packages.
    print(f"Python version: {sys.version}")
    #print(f"Pytorch version: {torch.__version__}")
    #print(f"Numpy version: {np.__version__}")
    #print(f"Seaborn version: {sn.__version__}")
    #print(f"Pandas version: {pd.__version__}")
    #print(f"Matplotlib version: {matplotlib.__version__}")
    # Generate signal and plot it
    s, t = pp(f,T,fs)
    plt.plot(t, s, 'o-')
    #plt.show()


    # A new version to find module versions automatically. TODO: what about modules that do not have version in __version__
    modulenames = list(imports())
    modulenames = list(set(modulenames))
    for m in modulenames:
        try:
            version_id = eval(m).__version__
            print(f"Module {m} version: {version_id}")
        except (AttributeError, NameError):
            #print(f"No version info for module {m} in .__version__")
            continue
    pass