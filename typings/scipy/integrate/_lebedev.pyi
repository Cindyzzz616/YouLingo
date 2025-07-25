"""
This type stub file was generated by pyright.
"""

__all__ = ['lebedev_rule']
def get_lebedev_sphere(degree):
    class Leb:
        ...
    
    

def get_lebedev_recurrence_points(type_, start, a, b, v, leb): # -> tuple[Any, Any]:
    ...

def lebedev_rule(n): # -> tuple[NDArray[Any], Any]:
    r"""Lebedev quadrature.

    Compute the sample points and weights for Lebedev quadrature [1]_
    for integration of a function over the surface of a unit sphere.

    Parameters
    ----------
    n : int
        Quadrature order. See Notes for supported values.

    Returns
    -------
    x : ndarray of shape ``(3, m)``
        Sample points on the unit sphere in Cartesian coordinates.
        ``m`` is the "degree" corresponding with the specified order; see Notes.
    w : ndarray of shape ``(m,)``
        Weights

    Notes
    -----
    Implemented by translating the Matlab code of [2]_ to Python.

    The available orders (argument `n`) are::

        3, 5, 7, 9, 11, 13, 15, 17,
        19, 21, 23, 25, 27, 29, 31, 35,
        41, 47, 53, 59, 65, 71, 77, 83,
        89, 95, 101, 107, 113, 119, 125, 131

    The corresponding degrees ``m`` are::

        6, 14, 26, 38, 50, 74, 86, 110,
        146, 170, 194, 230, 266, 302, 350, 434,
        590, 770, 974, 1202, 1454, 1730, 2030, 2354,
        2702, 3074, 3470, 3890, 4334, 4802, 5294, 5810

    References
    ----------
    .. [1] V.I. Lebedev, and D.N. Laikov. "A quadrature formula for the sphere of
           the 131st algebraic order of accuracy". Doklady Mathematics, Vol. 59,
           No. 3, 1999, pp. 477-481.
    .. [2] R. Parrish. ``getLebedevSphere``. Matlab Central File Exchange.
           https://www.mathworks.com/matlabcentral/fileexchange/27097-getlebedevsphere.
    .. [3] Bellet, Jean-Baptiste, Matthieu Brachet, and Jean-Pierre Croisille.
           "Quadrature and symmetry on the Cubed Sphere." Journal of Computational and
           Applied Mathematics 409 (2022): 114142. :doi:`10.1016/j.cam.2022.114142`.

    Examples
    --------
    An example given in [3]_ is integration of :math:`f(x, y, z) = \exp(x)` over a
    sphere of radius :math:`1`; the reference there is ``14.7680137457653``.
    Show the convergence to the expected result as the order increases:

    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> from scipy.integrate import lebedev_rule
    >>>
    >>> def f(x):
    ...     return np.exp(x[0])
    >>>
    >>> res = []
    >>> orders = np.arange(3, 20, 2)
    >>> for n in orders:
    ...     x, w = lebedev_rule(n)
    ...     res.append(w @ f(x))
    >>>
    >>> ref = np.full_like(res, 14.7680137457653)
    >>> err = abs(res - ref)/abs(ref)
    >>> plt.semilogy(orders, err)
    >>> plt.xlabel('order $n$')
    >>> plt.ylabel('relative error')
    >>> plt.title(r'Convergence for $f(x, y, z) = \exp(x)$')
    >>> plt.show()

    """
    ...

