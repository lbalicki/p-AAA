import numpy as np

from paaa import pAAAReductor
from pymor.models.transfer_function import TransferFunction


def H(s, p, z):
    return np.tensordot(1/(1+25*(s+p)**2) + 0.5/(1+25*(s-0.5)**2) + 0.1/(p+25) + z**2 + 1, np.eye(2), 0)


S = [np.linspace(-1, 1, 11),  np.linspace(0, 1, 11), np.linspace(1, 2, 11)]

fom = TransferFunction(2, 2, lambda s, mu: H(s, mu['p'], mu['z']), parameters={'p': 1, 'z': 1})
paaa = pAAAReductor(data=S, fom=fom)
rom = paaa.reduce(tol=1e-12)
