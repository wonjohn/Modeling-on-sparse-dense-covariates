#-------------------------------------------------------------------------------
# Name:        Learning spatial processes through sparse measurements 
#              and its dense gridded covariate(s)

##########
# Gridded covariate(s)
##########


# Purpose:     
#              1. Aiming at the general problem of populating sparse in-situs with EO data
#              2. Starting from artificially created dummy data
#              3. Deducting the problems to special study cases
#              Main method is ...
#
# Modifications ~~:
#              1.
#
# Author:      Jiong Wang
#
# Created:     08/01/2020
# Copyright:   (c) JonWang 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from agroundTruth import *
from pt import *

#==================================
# 02_4 Dense covariate from the ground truth processes
#==================================
# One handy option is to generate covariate(s) through linear transformation.
# Other options can be insufficient observations or other components to be involved.
# The most ideal result should give a strong free form coregionalization matrix
# B = WW', where, as B is normalized to correlation, the diagonal is close to 1.

# Generate dense covariate through linear transformation of the ground truth GP
# Scale, shift in x1, x2, and y, convolution and etc..
def linCov(X,Y):
    scale = np.linspace(-2,2,1)
    for s in scale:
        print('Scale Y by ', s)
        Ys = Y*s
        showGrid(X, Ys)
    return (X, Ys)


# Generate dense covariate as a insufficient observation of the ground truth GP
def insuffCov(X,Y,n):
    r, c = int(np.sqrt(X.shape[0])*s), int(np.sqrt(X.shape[0])*s)  # Rows and columns with scaled density
    # Insufficiently observed points
    x, y = randPt(X,Y,n)
    # A proximation of the ground truth through few points
    Xp, Yp, m = gtGP(x, y, r, c)  # Take advantage of the gtGP function
    return (Xp, Yp)
