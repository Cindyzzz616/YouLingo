"""
This type stub file was generated by pyright.
"""

'''
This module contains subroutines concerning the geometry-improving of the interpolation set.

Translated from Zaikun Zhang's modern-Fortran reference implementation in PRIMA.

Dedicated to late Professor M. J. D. Powell FRS (1936--2015).

Python translation by Nickolai Belakovski.
'''
def setdrop_tr(ximproved, d, delta, rho, sim, simi): # -> intp | None:
    '''
    This function finds (the index) of a current interpolation point to be replaced with
    the trust-region trial point. See (19)-(22) of the COBYLA paper.
    N.B.:
    1. If XIMPROVED == True, then JDROP > 0 so that D is included into XPT. Otherwise,
       it is a bug.
    2. COBYLA never sets JDROP = NUM_VARS
    TODO: Check whether it improves the performance if JDROP = NUM_VARS is allowed when
    XIMPROVED is True. Note that UPDATEXFC should be revised accordingly.
    '''
    ...

def geostep(jdrop, amat, bvec, conmat, cpen, cval, delbar, fval, simi):
    '''
    This function calculates a geometry step so that the geometry of the interpolation set is improved
    when SIM[: JDROP_GEO] is replaced with SIM[:, NUM_VARS] + D. See (15)--(17) of the COBYLA paper.
    '''
    ...

