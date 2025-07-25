"""
This type stub file was generated by pyright.
"""

'''
This module provides some basic linear algebra procedures.

Translated from Zaikun Zhang's modern-Fortran reference implementation in PRIMA.

Dedicated to late Professor M. J. D. Powell FRS (1936--2015).

Python translation by Nickolai Belakovski.
'''
USE_NAIVE_MATH = ...
def inprod(x, y): # -> Any | Literal[0]:
    ...

def matprod12(x, y): # -> NDArray[float64]:
    ...

def matprod21(x, y): # -> NDArray[float64]:
    ...

def matprod22(x, y): # -> _Array[tuple[int, int], float64]:
    ...

def matprod(x, y): # -> Any | NDArray[float64] | _Array[tuple[int, int], float64] | Literal[0]:
    ...

def outprod(x, y): # -> NDArray[Any] | _Array[tuple[int, int], float64]:
    ...

def lsqr(A, b, Q, Rdiag): # -> NDArray[float64]:
    ...

def hypot(x1, x2): # -> Any | Literal[0]:
    ...

def norm(x): # -> floating[Any] | Any:
    ...

def istril(A, tol=...): # -> builtins.bool | NDArray[numpy.bool[builtins.bool]]:
    ...

def istriu(A, tol=...): # -> builtins.bool | NDArray[numpy.bool[builtins.bool]]:
    ...

def inv(A): # -> _Array[tuple[int, int], float64] | ndarray[_Shape, dtype[float64]]:
    ...

def qr(A): # -> tuple[NDArray[float64], Any, NDArray[Any]]:
    ...

def primasum(x, axis=...): # -> int | NDArray[float64] | None:
    '''
    According to its documentation, np.sum will sometimes do partial pairwise summation.
    For our purposes, when comparing, we want don't want to do anything fancy, and we
    just want to add things up one at a time.
    '''
    ...

def primapow2(x):
    '''
    Believe it or now, x**2 is not always the same as x*x in Python. In Fortran they
    appear to be identical. Here's a quick one-line to find an example on your system
    (well, two liner after importing numpy):
    list(filter(lambda x: x[1], [(x:=np.random.random(), x**2 - x*x != 0) for _ in range(10000)]))
    '''
    ...

def planerot(x): # -> NDArray[Any]:
    '''
    As in MATLAB, planerot(x) returns a 2x2 Givens matrix G for x in R2 so that Y=G@x has Y[1] = 0.
    Roughly speaking, G = np.array([[x[0]/R, x[1]/R], [-x[1]/R, x[0]/R]]), where R = np.linalg.norm(x).
    0. We need to take care of the possibilities of R=0, Inf, NaN, and over/underflow.
    1. The G defined above is continuous with respect to X except at 0. Following this definition,
    G = np.array([[np.sign(x[0]), 0], [0, np.sign(x[0])]]) if x[1] == 0,
    G = np.array([[0, np.sign(x[1])], [np.sign(x[1]), 0]]) if x[0] == 0
    Yet some implementations ignore the signs, leading to discontinuity and numerical instability.
    2. Difference from MATLAB: if x contains NaN of consists of only Inf, MATLAB returns a NaN matrix,
    but we return an identity matrix or a matrix of +/-np.sqrt(2). We intend to keep G always orthogonal.
    '''
    ...

def isminor(x, ref): # -> Any:
    '''
    This function tests whether x is minor compared to ref. It is used by Powell, e.g., in COBYLA.
    In precise arithmetic, isminor(x, ref) is true if and only if x == 0; in floating point
    arithmetic, isminor(x, ref) is true if x is 0 or its nonzero value can be attributed to
    computer rounding errors according to ref.
    Larger sensitivity means the function is more strict/precise, the value 0.1 being due to Powell.

    For example:
    isminor(1e-20, 1e300) -> True, because in floating point arithmetic 1e-20 cannot be added to
    1e300 without being rounded to 1e300.
    isminor(1e300, 1e-20) -> False, because in floating point arithmetic adding 1e300 to 1e-20
    dominates the latter number.
    isminor(3, 4) -> False, because 3 can be added to 4 without being rounded off
    '''
    ...

def isinv(A, B, tol=...):
    '''
    This procedure tests whether A = B^{-1} up to the tolerance TOL.
    '''
    ...

def isorth(A, tol=...): # -> numpy.bool[builtins.bool] | Literal[False]:
    '''
    This function tests whether the matrix A has orthonormal columns up to the tolerance TOL.
    '''
    ...

def get_arrays_tol(*arrays): # -> Any:
    """
    Get a relative tolerance for a set of arrays. Borrowed from COBYQA

    Parameters
    ----------
    *arrays: tuple
        Set of `numpy.ndarray` to get the tolerance for.

    Returns
    -------
    float
        Relative tolerance for the set of arrays.

    Raises
    ------
    ValueError
        If no array is provided.
    """
    ...

