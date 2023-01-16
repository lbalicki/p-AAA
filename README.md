# p-AAA

The most up-to-date implementation of the algorithm is now part of the [pyMOR](https://github.com/pymor/pymor) repository ([pAAA implementation](https://github.com/pymor/pymor/blob/main/src/pymor/reductors/aaa.py)) and includes bug-fixes as well as other improvements.

This repository contains an implementation of the parametric AAA (p-AAA) algorithm from:
<br /> <br />
The p-AAA algorithm for data driven modeling of parametric dynamical systems <br />
Andrea Carracedo Rodriguez, Linus Balicki, Serkan Gugercin <br />
2022, https://doi.org/10.48550/arXiv.2003.06536 <br />

The scripts "test_heat_LTI.py", "test_synthetic_tf_MIMO.py" and "test_synthetic_tf_SISO.py" showcase different examples.

# Installation

Python version 3.7 or higher should be used. The necessary packages are listed in requirements.txt and can be installed, e.g. via running

`pip install -r requirements.txt`

in the installation folder.

# License

The code is available under the MIT license.
