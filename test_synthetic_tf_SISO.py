import numpy as np

from paaa import pAAAReductor


def H(s, p):
    return 1/(1+25*(s+p)**2) + 0.5/(1+25*(s-0.5)**2) + 0.1/(p+25)


S = [np.linspace(-1, 1, 21),  np.linspace(0, 1, 21)]
S0, S1 = np.meshgrid(S[0], S[1], indexing='ij')

Phi = H(S0, S1)

paaa = pAAAReductor(data=(S, Phi))
rom = paaa.reduce(tol=1e-12)
