"""
This type stub file was generated by pyright.
"""

"""
fitpack (dierckx in netlib) --- A Python-C wrapper to FITPACK (by P. Dierckx).
        FITPACK is a collection of FORTRAN programs for curve and surface
        fitting with splines and tensor product splines.

See
 https://web.archive.org/web/20010524124604/http://www.cs.kuleuven.ac.be:80/cwis/research/nalag/research/topics/fitpack.html
or
 http://www.netlib.org/dierckx/

Copyright 2002 Pearu Peterson all rights reserved,
Pearu Peterson <pearu@cens.ioc.ee>
Permission to use, modify, and distribute this software is given under the
terms of the SciPy (BSD style) license. See LICENSE.txt that came with
this distribution for specifics.

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.

TODO: Make interfaces to the following fitpack functions:
    For univariate splines: cocosp, concon, fourco, insert
    For bivariate splines: profil, regrid, parsur, surev
"""
__all__ = ['splrep', 'splprep', 'splev', 'splint', 'sproot', 'spalde', 'bisplrep', 'bisplev', 'insert', 'splder', 'splantider']
dfitpack_int = ...
_iermess = ...
_iermess2 = ...
_parcur_cache = ...
def splprep(x, w=..., u=..., ub=..., ue=..., k=..., task=..., s=..., t=..., full_output=..., nest=..., per=..., quiet=...):
    ...

_curfit_cache = ...
def splrep(x, y, w=..., xb=..., xe=..., k=..., task=..., s=..., t=..., full_output=..., per=..., quiet=...): # -> tuple[tuple[Any, Any, int], Any, Any, Any] | tuple[Any, Any, int]:
    ...

def splev(x, tck, der=..., ext=...): # -> list[Any]:
    ...

def splint(a, b, tck, full_output=...): # -> list[Any] | tuple[Any, Any]:
    ...

def sproot(tck, mest=...): # -> list[Any]:
    ...

def spalde(x, tck): # -> list[Any] | list[list[Any] | Any]:
    ...

_surfit_cache = ...
def bisplrep(x, y, z, w=..., xb=..., xe=..., yb=..., ye=..., kx=..., ky=..., task=..., s=..., eps=..., tx=..., ty=..., full_output=..., nxest=..., nyest=..., quiet=...):
    """
    Find a bivariate B-spline representation of a surface.

    Given a set of data points (x[i], y[i], z[i]) representing a surface
    z=f(x,y), compute a B-spline representation of the surface. Based on
    the routine SURFIT from FITPACK.

    Parameters
    ----------
    x, y, z : ndarray
        Rank-1 arrays of data points.
    w : ndarray, optional
        Rank-1 array of weights. By default ``w=np.ones(len(x))``.
    xb, xe : float, optional
        End points of approximation interval in `x`.
        By default ``xb = x.min(), xe=x.max()``.
    yb, ye : float, optional
        End points of approximation interval in `y`.
        By default ``yb=y.min(), ye = y.max()``.
    kx, ky : int, optional
        The degrees of the spline (1 <= kx, ky <= 5).
        Third order (kx=ky=3) is recommended.
    task : int, optional
        If task=0, find knots in x and y and coefficients for a given
        smoothing factor, s.
        If task=1, find knots and coefficients for another value of the
        smoothing factor, s.  bisplrep must have been previously called
        with task=0 or task=1.
        If task=-1, find coefficients for a given set of knots tx, ty.
    s : float, optional
        A non-negative smoothing factor. If weights correspond
        to the inverse of the standard-deviation of the errors in z,
        then a good s-value should be found in the range
        ``(m-sqrt(2*m),m+sqrt(2*m))`` where m=len(x).
    eps : float, optional
        A threshold for determining the effective rank of an
        over-determined linear system of equations (0 < eps < 1).
        `eps` is not likely to need changing.
    tx, ty : ndarray, optional
        Rank-1 arrays of the knots of the spline for task=-1
    full_output : int, optional
        Non-zero to return optional outputs.
    nxest, nyest : int, optional
        Over-estimates of the total number of knots. If None then
        ``nxest = max(kx+sqrt(m/2),2*kx+3)``,
        ``nyest = max(ky+sqrt(m/2),2*ky+3)``.
    quiet : int, optional
        Non-zero to suppress printing of messages.

    Returns
    -------
    tck : array_like
        A list [tx, ty, c, kx, ky] containing the knots (tx, ty) and
        coefficients (c) of the bivariate B-spline representation of the
        surface along with the degree of the spline.
    fp : ndarray
        The weighted sum of squared residuals of the spline approximation.
    ier : int
        An integer flag about splrep success. Success is indicated if
        ier<=0. If ier in [1,2,3] an error occurred but was not raised.
        Otherwise an error is raised.
    msg : str
        A message corresponding to the integer flag, ier.

    See Also
    --------
    splprep, splrep, splint, sproot, splev
    UnivariateSpline, BivariateSpline

    Notes
    -----
    See `bisplev` to evaluate the value of the B-spline given its tck
    representation.

    If the input data is such that input dimensions have incommensurate
    units and differ by many orders of magnitude, the interpolant may have
    numerical artifacts. Consider rescaling the data before interpolation.

    References
    ----------
    .. [1] Dierckx P.:An algorithm for surface fitting with spline functions
       Ima J. Numer. Anal. 1 (1981) 267-283.
    .. [2] Dierckx P.:An algorithm for surface fitting with spline functions
       report tw50, Dept. Computer Science,K.U.Leuven, 1980.
    .. [3] Dierckx P.:Curve and surface fitting with splines, Monographs on
       Numerical Analysis, Oxford University Press, 1993.

    Examples
    --------
    Examples are given :ref:`in the tutorial <tutorial-interpolate_2d_spline>`.

    """
    ...

def bisplev(x, y, tck, dx=..., dy=...):
    """
    Evaluate a bivariate B-spline and its derivatives.

    Return a rank-2 array of spline function values (or spline derivative
    values) at points given by the cross-product of the rank-1 arrays `x` and
    `y`.  In special cases, return an array or just a float if either `x` or
    `y` or both are floats.  Based on BISPEV and PARDER from FITPACK.

    Parameters
    ----------
    x, y : ndarray
        Rank-1 arrays specifying the domain over which to evaluate the
        spline or its derivative.
    tck : tuple
        A sequence of length 5 returned by `bisplrep` containing the knot
        locations, the coefficients, and the degree of the spline:
        [tx, ty, c, kx, ky].
    dx, dy : int, optional
        The orders of the partial derivatives in `x` and `y` respectively.

    Returns
    -------
    vals : ndarray
        The B-spline or its derivative evaluated over the set formed by
        the cross-product of `x` and `y`.

    See Also
    --------
    splprep, splrep, splint, sproot, splev
    UnivariateSpline, BivariateSpline

    Notes
    -----
        See `bisplrep` to generate the `tck` representation.

    References
    ----------
    .. [1] Dierckx P. : An algorithm for surface fitting
       with spline functions
       Ima J. Numer. Anal. 1 (1981) 267-283.
    .. [2] Dierckx P. : An algorithm for surface fitting
       with spline functions
       report tw50, Dept. Computer Science,K.U.Leuven, 1980.
    .. [3] Dierckx P. : Curve and surface fitting with splines,
       Monographs on Numerical Analysis, Oxford University Press, 1993.

    Examples
    --------
    Examples are given :ref:`in the tutorial <tutorial-interpolate_2d_spline>`.

    """
    ...

def dblint(xa, xb, ya, yb, tck):
    """Evaluate the integral of a spline over area [xa,xb] x [ya,yb].

    Parameters
    ----------
    xa, xb : float
        The end-points of the x integration interval.
    ya, yb : float
        The end-points of the y integration interval.
    tck : list [tx, ty, c, kx, ky]
        A sequence of length 5 returned by bisplrep containing the knot
        locations tx, ty, the coefficients c, and the degrees kx, ky
        of the spline.

    Returns
    -------
    integ : float
        The value of the resulting integral.
    """
    ...

def insert(x, tck, m=..., per=...): # -> tuple[Any, list[Any], Any] | tuple[Any, Any, Any]:
    ...

def splder(tck, n=...): # -> tuple[Any, Any | Incomplete, Any]:
    ...

def splantider(tck, n=...): # -> tuple[Any, Any | Incomplete, Any] | tuple[Any | Incomplete, Any | Incomplete, Any]:
    ...

