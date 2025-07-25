"""
This type stub file was generated by pyright.
"""

"""Basic linear factorizations needed by the solver."""
sksparse_available = ...
__all__ = ['orthogonality', 'projections']
def orthogonality(A, g): # -> floating[Any] | Any | Literal[0]:
    """Measure orthogonality between a vector and the null space of a matrix.

    Compute a measure of orthogonality between the null space
    of the (possibly sparse) matrix ``A`` and a given vector ``g``.

    The formula is a simplified (and cheaper) version of formula (3.13)
    from [1]_.
    ``orth =  norm(A g, ord=2)/(norm(A, ord='fro')*norm(g, ord=2))``.

    References
    ----------
    .. [1] Gould, Nicholas IM, Mary E. Hribar, and Jorge Nocedal.
           "On the solution of equality constrained quadratic
            programming problems arising in optimization."
            SIAM Journal on Scientific Computing 23.4 (2001): 1376-1395.
    """
    ...

def normal_equation_projections(A, m, n, orth_tol, max_refin, tol): # -> tuple[Callable[..., Any], Callable[..., Any], Callable[..., Any]]:
    """Return linear operators for matrix A using ``NormalEquation`` approach.
    """
    ...

def augmented_system_projections(A, m, n, orth_tol, max_refin, tol): # -> tuple[Callable[..., Any], Callable[..., Any], Callable[..., Any]]:
    """Return linear operators for matrix A - ``AugmentedSystem``."""
    ...

def qr_factorization_projections(A, m, n, orth_tol, max_refin, tol): # -> tuple[Callable[..., Any], Callable[..., Any], Callable[..., Any]] | tuple[Callable[..., Any], Callable[..., NDArray[float64]], Callable[..., Any]]:
    """Return linear operators for matrix A using ``QRFactorization`` approach.
    """
    ...

def svd_factorization_projections(A, m, n, orth_tol, max_refin, tol): # -> tuple[Callable[..., Any], Callable[..., Any], Callable[..., Any]]:
    """Return linear operators for matrix A using ``SVDFactorization`` approach.
    """
    ...

def projections(A, method=..., orth_tol=..., max_refin=..., tol=...): # -> tuple[LinearOperator, LinearOperator, LinearOperator]:
    """Return three linear operators related with a given matrix A.

    Parameters
    ----------
    A : sparse array (or ndarray), shape (m, n)
        Matrix ``A`` used in the projection.
    method : string, optional
        Method used for compute the given linear
        operators. Should be one of:

            - 'NormalEquation': The operators
               will be computed using the
               so-called normal equation approach
               explained in [1]_. In order to do
               so the Cholesky factorization of
               ``(A A.T)`` is computed. Exclusive
               for sparse matrices.
            - 'AugmentedSystem': The operators
               will be computed using the
               so-called augmented system approach
               explained in [1]_. Exclusive
               for sparse matrices.
            - 'QRFactorization': Compute projections
               using QR factorization. Exclusive for
               dense matrices.
            - 'SVDFactorization': Compute projections
               using SVD factorization. Exclusive for
               dense matrices.

    orth_tol : float, optional
        Tolerance for iterative refinements.
    max_refin : int, optional
        Maximum number of iterative refinements.
    tol : float, optional
        Tolerance for singular values.

    Returns
    -------
    Z : LinearOperator, shape (n, n)
        Null-space operator. For a given vector ``x``,
        the null space operator is equivalent to apply
        a projection matrix ``P = I - A.T inv(A A.T) A``
        to the vector. It can be shown that this is
        equivalent to project ``x`` into the null space
        of A.
    LS : LinearOperator, shape (m, n)
        Least-squares operator. For a given vector ``x``,
        the least-squares operator is equivalent to apply a
        pseudoinverse matrix ``pinv(A.T) = inv(A A.T) A``
        to the vector. It can be shown that this vector
        ``pinv(A.T) x`` is the least_square solution to
        ``A.T y = x``.
    Y : LinearOperator, shape (n, m)
        Row-space operator. For a given vector ``x``,
        the row-space operator is equivalent to apply a
        projection matrix ``Q = A.T inv(A A.T)``
        to the vector.  It can be shown that this
        vector ``y = Q x``  the minimum norm solution
        of ``A y = x``.

    Notes
    -----
    Uses iterative refinements described in [1]
    during the computation of ``Z`` in order to
    cope with the possibility of large roundoff errors.

    References
    ----------
    .. [1] Gould, Nicholas IM, Mary E. Hribar, and Jorge Nocedal.
        "On the solution of equality constrained quadratic
        programming problems arising in optimization."
        SIAM Journal on Scientific Computing 23.4 (2001): 1376-1395.
    """
    ...

