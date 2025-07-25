"""
This type stub file was generated by pyright.
"""

noScikit = ...
useUmfpack = ...
__all__ = ['use_solver', 'spsolve', 'splu', 'spilu', 'factorized', 'MatrixRankWarning', 'spsolve_triangular', 'is_sptriangular', 'spbandwidth']
class MatrixRankWarning(UserWarning):
    """Warning for exactly singular matrices."""
    ...


def use_solver(**kwargs): # -> None:
    """
    Select default sparse direct solver to be used.

    Parameters
    ----------
    useUmfpack : bool, optional
        Use UMFPACK [1]_, [2]_, [3]_, [4]_. over SuperLU. Has effect only
        if ``scikits.umfpack`` is installed. Default: True
    assumeSortedIndices : bool, optional
        Allow UMFPACK to skip the step of sorting indices for a CSR/CSC matrix.
        Has effect only if useUmfpack is True and ``scikits.umfpack`` is
        installed. Default: False

    Notes
    -----
    The default sparse solver is UMFPACK when available
    (``scikits.umfpack`` is installed). This can be changed by passing
    useUmfpack = False, which then causes the always present SuperLU
    based solver to be used.

    UMFPACK requires a CSR/CSC matrix to have sorted column/row indices. If
    sure that the matrix fulfills this, pass ``assumeSortedIndices=True``
    to gain some speed.

    References
    ----------
    .. [1] T. A. Davis, Algorithm 832:  UMFPACK - an unsymmetric-pattern
           multifrontal method with a column pre-ordering strategy, ACM
           Trans. on Mathematical Software, 30(2), 2004, pp. 196--199.
           https://dl.acm.org/doi/abs/10.1145/992200.992206

    .. [2] T. A. Davis, A column pre-ordering strategy for the
           unsymmetric-pattern multifrontal method, ACM Trans.
           on Mathematical Software, 30(2), 2004, pp. 165--195.
           https://dl.acm.org/doi/abs/10.1145/992200.992205

    .. [3] T. A. Davis and I. S. Duff, A combined unifrontal/multifrontal
           method for unsymmetric sparse matrices, ACM Trans. on
           Mathematical Software, 25(1), 1999, pp. 1--19.
           https://doi.org/10.1145/305658.287640

    .. [4] T. A. Davis and I. S. Duff, An unsymmetric-pattern multifrontal
           method for sparse LU factorization, SIAM J. Matrix Analysis and
           Computations, 18(1), 1997, pp. 140--158.
           https://doi.org/10.1137/S0895479894246905T.

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse.linalg import use_solver, spsolve
    >>> from scipy.sparse import csc_array
    >>> R = np.random.randn(5, 5)
    >>> A = csc_array(R)
    >>> b = np.random.randn(5)
    >>> use_solver(useUmfpack=False) # enforce superLU over UMFPACK
    >>> x = spsolve(A, b)
    >>> np.allclose(A.dot(x), b)
    True
    >>> use_solver(useUmfpack=True) # reset umfPack usage to default
    """
    ...

def spsolve(A, b, permc_spec=..., use_umfpack=...): # -> csc_array | Any:
    """Solve the sparse linear system Ax=b, where b may be a vector or a matrix.

    Parameters
    ----------
    A : ndarray or sparse array or matrix
        The square matrix A will be converted into CSC or CSR form
    b : ndarray or sparse array or matrix
        The matrix or vector representing the right hand side of the equation.
        If a vector, b.shape must be (n,) or (n, 1).
    permc_spec : str, optional
        How to permute the columns of the matrix for sparsity preservation.
        (default: 'COLAMD')

        - ``NATURAL``: natural ordering.
        - ``MMD_ATA``: minimum degree ordering on the structure of A^T A.
        - ``MMD_AT_PLUS_A``: minimum degree ordering on the structure of A^T+A.
        - ``COLAMD``: approximate minimum degree column ordering [1]_, [2]_.

    use_umfpack : bool, optional
        if True (default) then use UMFPACK for the solution [3]_, [4]_, [5]_,
        [6]_ . This is only referenced if b is a vector and
        ``scikits.umfpack`` is installed.

    Returns
    -------
    x : ndarray or sparse array or matrix
        the solution of the sparse linear equation.
        If b is a vector, then x is a vector of size A.shape[1]
        If b is a matrix, then x is a matrix of size (A.shape[1], b.shape[1])

    Notes
    -----
    For solving the matrix expression AX = B, this solver assumes the resulting
    matrix X is sparse, as is often the case for very sparse inputs.  If the
    resulting X is dense, the construction of this sparse result will be
    relatively expensive.  In that case, consider converting A to a dense
    matrix and using scipy.linalg.solve or its variants.

    References
    ----------
    .. [1] T. A. Davis, J. R. Gilbert, S. Larimore, E. Ng, Algorithm 836:
           COLAMD, an approximate column minimum degree ordering algorithm,
           ACM Trans. on Mathematical Software, 30(3), 2004, pp. 377--380.
           :doi:`10.1145/1024074.1024080`

    .. [2] T. A. Davis, J. R. Gilbert, S. Larimore, E. Ng, A column approximate
           minimum degree ordering algorithm, ACM Trans. on Mathematical
           Software, 30(3), 2004, pp. 353--376. :doi:`10.1145/1024074.1024079`

    .. [3] T. A. Davis, Algorithm 832:  UMFPACK - an unsymmetric-pattern
           multifrontal method with a column pre-ordering strategy, ACM
           Trans. on Mathematical Software, 30(2), 2004, pp. 196--199.
           https://dl.acm.org/doi/abs/10.1145/992200.992206

    .. [4] T. A. Davis, A column pre-ordering strategy for the
           unsymmetric-pattern multifrontal method, ACM Trans.
           on Mathematical Software, 30(2), 2004, pp. 165--195.
           https://dl.acm.org/doi/abs/10.1145/992200.992205

    .. [5] T. A. Davis and I. S. Duff, A combined unifrontal/multifrontal
           method for unsymmetric sparse matrices, ACM Trans. on
           Mathematical Software, 25(1), 1999, pp. 1--19.
           https://doi.org/10.1145/305658.287640

    .. [6] T. A. Davis and I. S. Duff, An unsymmetric-pattern multifrontal
           method for sparse LU factorization, SIAM J. Matrix Analysis and
           Computations, 18(1), 1997, pp. 140--158.
           https://doi.org/10.1137/S0895479894246905T.


    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import csc_array
    >>> from scipy.sparse.linalg import spsolve
    >>> A = csc_array([[3, 2, 0], [1, -1, 0], [0, 5, 1]], dtype=float)
    >>> B = csc_array([[2, 0], [-1, 0], [2, 0]], dtype=float)
    >>> x = spsolve(A, B)
    >>> np.allclose(A.dot(x).toarray(), B.toarray())
    True
    """
    ...

def splu(A, permc_spec=..., diag_pivot_thresh=..., relax=..., panel_size=..., options=...):
    """
    Compute the LU decomposition of a sparse, square matrix.

    Parameters
    ----------
    A : sparse array or matrix
        Sparse array to factorize. Most efficient when provided in CSC
        format. Other formats will be converted to CSC before factorization.
    permc_spec : str, optional
        How to permute the columns of the matrix for sparsity preservation.
        (default: 'COLAMD')

        - ``NATURAL``: natural ordering.
        - ``MMD_ATA``: minimum degree ordering on the structure of A^T A.
        - ``MMD_AT_PLUS_A``: minimum degree ordering on the structure of A^T+A.
        - ``COLAMD``: approximate minimum degree column ordering

    diag_pivot_thresh : float, optional
        Threshold used for a diagonal entry to be an acceptable pivot.
        See SuperLU user's guide for details [1]_
    relax : int, optional
        Expert option for customizing the degree of relaxing supernodes.
        See SuperLU user's guide for details [1]_
    panel_size : int, optional
        Expert option for customizing the panel size.
        See SuperLU user's guide for details [1]_
    options : dict, optional
        Dictionary containing additional expert options to SuperLU.
        See SuperLU user guide [1]_ (section 2.4 on the 'Options' argument)
        for more details. For example, you can specify
        ``options=dict(Equil=False, IterRefine='SINGLE'))``
        to turn equilibration off and perform a single iterative refinement.

    Returns
    -------
    invA : scipy.sparse.linalg.SuperLU
        Object, which has a ``solve`` method.

    See also
    --------
    spilu : incomplete LU decomposition

    Notes
    -----
    When a real array is factorized and the returned SuperLU object's ``solve()``
    method is used with complex arguments an error is generated. Instead, cast the
    initial array to complex and then factorize.

    This function uses the SuperLU library.

    References
    ----------
    .. [1] SuperLU https://portal.nersc.gov/project/sparse/superlu/

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import csc_array
    >>> from scipy.sparse.linalg import splu
    >>> A = csc_array([[1., 0., 0.], [5., 0., 2.], [0., -1., 0.]], dtype=float)
    >>> B = splu(A)
    >>> x = np.array([1., 2., 3.], dtype=float)
    >>> B.solve(x)
    array([ 1. , -3. , -1.5])
    >>> A.dot(B.solve(x))
    array([ 1.,  2.,  3.])
    >>> B.solve(A.dot(x))
    array([ 1.,  2.,  3.])
    """
    ...

def spilu(A, drop_tol=..., fill_factor=..., drop_rule=..., permc_spec=..., diag_pivot_thresh=..., relax=..., panel_size=..., options=...):
    """
    Compute an incomplete LU decomposition for a sparse, square matrix.

    The resulting object is an approximation to the inverse of `A`.

    Parameters
    ----------
    A : (N, N) array_like
        Sparse array to factorize. Most efficient when provided in CSC format.
        Other formats will be converted to CSC before factorization.
    drop_tol : float, optional
        Drop tolerance (0 <= tol <= 1) for an incomplete LU decomposition.
        (default: 1e-4)
    fill_factor : float, optional
        Specifies the fill ratio upper bound (>= 1.0) for ILU. (default: 10)
    drop_rule : str, optional
        Comma-separated string of drop rules to use.
        Available rules: ``basic``, ``prows``, ``column``, ``area``,
        ``secondary``, ``dynamic``, ``interp``. (Default: ``basic,area``)

        See SuperLU documentation for details.

    Remaining other options
        Same as for `splu`

    Returns
    -------
    invA_approx : scipy.sparse.linalg.SuperLU
        Object, which has a ``solve`` method.

    See also
    --------
    splu : complete LU decomposition

    Notes
    -----
    When a real array is factorized and the returned SuperLU object's ``solve()`` method
    is used with complex arguments an error is generated. Instead, cast the initial 
    array to complex and then factorize.

    To improve the better approximation to the inverse, you may need to
    increase `fill_factor` AND decrease `drop_tol`.

    This function uses the SuperLU library.

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import csc_array
    >>> from scipy.sparse.linalg import spilu
    >>> A = csc_array([[1., 0., 0.], [5., 0., 2.], [0., -1., 0.]], dtype=float)
    >>> B = spilu(A)
    >>> x = np.array([1., 2., 3.], dtype=float)
    >>> B.solve(x)
    array([ 1. , -3. , -1.5])
    >>> A.dot(B.solve(x))
    array([ 1.,  2.,  3.])
    >>> B.solve(A.dot(x))
    array([ 1.,  2.,  3.])
    """
    ...

def factorized(A): # -> Callable[..., Any]:
    """
    Return a function for solving a sparse linear system, with A pre-factorized.

    Parameters
    ----------
    A : (N, N) array_like
        Input. A in CSC format is most efficient. A CSR format matrix will
        be converted to CSC before factorization.

    Returns
    -------
    solve : callable
        To solve the linear system of equations given in `A`, the `solve`
        callable should be passed an ndarray of shape (N,).

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse.linalg import factorized
    >>> from scipy.sparse import csc_array
    >>> A = np.array([[ 3. ,  2. , -1. ],
    ...               [ 2. , -2. ,  4. ],
    ...               [-1. ,  0.5, -1. ]])
    >>> solve = factorized(csc_array(A)) # Makes LU decomposition.
    >>> rhs1 = np.array([1, -2, 0])
    >>> solve(rhs1) # Uses the LU factors.
    array([ 1., -2., -2.])

    """
    ...

def spsolve_triangular(A, b, lower=..., overwrite_A=..., overwrite_b=..., unit_diagonal=...):
    """
    Solve the equation ``A x = b`` for `x`, assuming A is a triangular matrix.

    Parameters
    ----------
    A : (M, M) sparse array or matrix
        A sparse square triangular matrix. Should be in CSR or CSC format.
    b : (M,) or (M, N) array_like
        Right-hand side matrix in ``A x = b``
    lower : bool, optional
        Whether `A` is a lower or upper triangular matrix.
        Default is lower triangular matrix.
    overwrite_A : bool, optional
        Allow changing `A`.
        Enabling gives a performance gain. Default is False.
    overwrite_b : bool, optional
        Allow overwriting data in `b`.
        Enabling gives a performance gain. Default is False.
        If `overwrite_b` is True, it should be ensured that
        `b` has an appropriate dtype to be able to store the result.
    unit_diagonal : bool, optional
        If True, diagonal elements of `a` are assumed to be 1.

        .. versionadded:: 1.4.0

    Returns
    -------
    x : (M,) or (M, N) ndarray
        Solution to the system ``A x = b``. Shape of return matches shape
        of `b`.

    Raises
    ------
    LinAlgError
        If `A` is singular or not triangular.
    ValueError
        If shape of `A` or shape of `b` do not match the requirements.

    Notes
    -----
    .. versionadded:: 0.19.0

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import csc_array
    >>> from scipy.sparse.linalg import spsolve_triangular
    >>> A = csc_array([[3, 0, 0], [1, -1, 0], [2, 0, 1]], dtype=float)
    >>> B = np.array([[2, 0], [-1, 0], [2, 0]], dtype=float)
    >>> x = spsolve_triangular(A, B)
    >>> np.allclose(A.dot(x), B)
    True
    """
    ...

def is_sptriangular(A): # -> tuple[Any, Any] | tuple[builtins.bool, builtins.bool] | tuple[Literal[False], Literal[False]] | tuple[numpy.bool[builtins.bool] | Any, numpy.bool[builtins.bool] | Any]:
    """Returns 2-tuple indicating lower/upper triangular structure for sparse ``A``

    Checks for triangular structure in ``A``. The result is summarized in
    two boolean values ``lower`` and ``upper`` to designate whether ``A`` is
    lower triangular or upper triangular respectively. Diagonal ``A`` will
    result in both being True. Non-triangular structure results in False for both.

    Only the sparse structure is used here. Values are not checked for zeros.

    This function will convert a copy of ``A`` to CSC format if it is not already
    CSR or CSC format. So it may be more efficient to convert it yourself if you
    have other uses for the CSR/CSC version.

    If ``A`` is not square, the portions outside the upper left square of the
    matrix do not affect its triangular structure. You probably want to work
    with the square portion of the matrix, though it is not requred here.

    Parameters
    ----------
    A : SciPy sparse array or matrix
        A sparse matrix preferrably in CSR or CSC format.

    Returns
    -------
    lower, upper : 2-tuple of bool

        .. versionadded:: 1.15.0

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import csc_array, eye_array
    >>> from scipy.sparse.linalg import is_sptriangular
    >>> A = csc_array([[3, 0, 0], [1, -1, 0], [2, 0, 1]], dtype=float)
    >>> is_sptriangular(A)
    (True, False)
    >>> D = eye_array(3, format='csr')
    >>> is_sptriangular(D)
    (True, True)
    """
    ...

def spbandwidth(A): # -> tuple[int, int] | tuple[Any, Any]:
    """Return the lower and upper bandwidth of a 2D numeric array.

    Computes the lower and upper limits on the bandwidth of the
    sparse 2D array ``A``. The result is summarized as a 2-tuple
    of positive integers ``(lo, hi)``. A zero denotes no sub/super
    diagonal entries on that side (tringular). The maximum value
    for ``lo``(``hi``) is one less than the number of rows(cols).

    Only the sparse structure is used here. Values are not checked for zeros.

    Parameters
    ----------
    A : SciPy sparse array or matrix
        A sparse matrix preferrably in CSR or CSC format.

    Returns
    -------
    below, above : 2-tuple of int
        The distance to the farthest non-zero diagonal below/above the
        main diagonal.

        .. versionadded:: 1.15.0

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse.linalg import spbandwidth
    >>> from scipy.sparse import csc_array, eye_array
    >>> A = csc_array([[3, 0, 0], [1, -1, 0], [2, 0, 1]], dtype=float)
    >>> spbandwidth(A)
    (2, 0)
    >>> D = eye_array(3, format='csr')
    >>> spbandwidth(D)
    (0, 0)
    """
    ...

