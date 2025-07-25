"""
This type stub file was generated by pyright.
"""

'''
This module contains subroutines concerning the update of the interpolation set.

Translated from Zaikun Zhang's modern-Fortran reference implementation in PRIMA.

Dedicated to late Professor M. J. D. Powell FRS (1936--2015).

Python translation by Nickolai Belakovski.
'''
def updatexfc(jdrop, constr, cpen, cstrv, d, f, conmat, cval, fval, sim, simi): # -> tuple[Any, Any, Any, Any, Any, Literal[0]] | tuple[Any, Any | _Array[tuple[int, int], float64] | ndarray[_Shape, dtype[float64]], Any, Any, Any, Literal[0, 7]]:
    '''
    This function revises the simplex by updating the elements of SIM, SIMI, FVAL, CONMAT, and CVAL
    '''
    ...

def findpole(cpen, cval, fval): # -> int:
    '''
    This subroutine identifies the best vertex of the current simplex with respect to the merit
    function PHI = F + CPEN * CSTRV.
    '''
    ...

def updatepole(cpen, conmat, cval, fval, sim, simi): # -> tuple[Any, Any, Any, Any, Any | _Array[tuple[int, int], float64] | ndarray[_Shape, dtype[float64]], Literal[0, 7]]:
    ...

