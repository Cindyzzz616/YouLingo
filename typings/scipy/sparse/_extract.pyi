"""
This type stub file was generated by pyright.
"""

"""Functions to extract parts of sparse matrices
"""
__docformat__ = ...
__all__ = ['find', 'tril', 'triu']
def find(A): # -> tuple[ndarray[_Shape, dtype[signedinteger[_32Bit] | signedinteger[_64Bit]]] | Any | ndarray[_Shape, dtype[signedinteger[_64Bit]]] | ndarray[_Shape, dtype[Any]] | ndarray[_Shape, dtype[intp]], ndarray[_Shape, dtype[signedinteger[_32Bit] | signedinteger[_64Bit]]] | Any | ndarray[_Shape, dtype[Any]], ndarray[_Shape, dtype[float64 | int_ | numpy.bool[builtins.bool]]] | ndarray[_Shape, Any] | Any | ndarray[_Shape, dtype[Any]]]:
    """Return the indices and values of the nonzero elements of a matrix

    Parameters
    ----------
    A : dense or sparse array or matrix
        Matrix whose nonzero elements are desired.

    Returns
    -------
    (I,J,V) : tuple of arrays
        I,J, and V contain the row indices, column indices, and values
        of the nonzero entries.


    Examples
    --------
    >>> from scipy.sparse import csr_array, find
    >>> A = csr_array([[7.0, 8.0, 0],[0, 0, 9.0]])
    >>> find(A)
    (array([0, 0, 1], dtype=int32),
     array([0, 1, 2], dtype=int32),
     array([ 7.,  8.,  9.]))

    """
    ...

def tril(A, k=..., format=...): # -> coo_array | Any | coo_matrix:
    """Return the lower triangular portion of a sparse array or matrix

    Returns the elements on or below the k-th diagonal of A.
        - k = 0 corresponds to the main diagonal
        - k > 0 is above the main diagonal
        - k < 0 is below the main diagonal

    Parameters
    ----------
    A : dense or sparse array or matrix
        Matrix whose lower trianglar portion is desired.
    k : integer : optional
        The top-most diagonal of the lower triangle.
    format : string
        Sparse format of the result, e.g. format="csr", etc.

    Returns
    -------
    L : sparse matrix
        Lower triangular portion of A in sparse format.

    See Also
    --------
    triu : upper triangle in sparse format

    Examples
    --------
    >>> from scipy.sparse import csr_array, tril
    >>> A = csr_array([[1, 2, 0, 0, 3], [4, 5, 0, 6, 7], [0, 0, 8, 9, 0]],
    ...               dtype='int32')
    >>> A.toarray()
    array([[1, 2, 0, 0, 3],
           [4, 5, 0, 6, 7],
           [0, 0, 8, 9, 0]], dtype=int32)
    >>> tril(A).toarray()
    array([[1, 0, 0, 0, 0],
           [4, 5, 0, 0, 0],
           [0, 0, 8, 0, 0]], dtype=int32)
    >>> tril(A).nnz
    4
    >>> tril(A, k=1).toarray()
    array([[1, 2, 0, 0, 0],
           [4, 5, 0, 0, 0],
           [0, 0, 8, 9, 0]], dtype=int32)
    >>> tril(A, k=-1).toarray()
    array([[0, 0, 0, 0, 0],
           [4, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]], dtype=int32)
    >>> tril(A, format='csc')
    <Compressed Sparse Column sparse array of dtype 'int32'
        with 4 stored elements and shape (3, 5)>

    """
    ...

def triu(A, k=..., format=...): # -> coo_array | Any | coo_matrix:
    """Return the upper triangular portion of a sparse array or matrix

    Returns the elements on or above the k-th diagonal of A.
        - k = 0 corresponds to the main diagonal
        - k > 0 is above the main diagonal
        - k < 0 is below the main diagonal

    Parameters
    ----------
    A : dense or sparse array or matrix
        Matrix whose upper trianglar portion is desired.
    k : integer : optional
        The bottom-most diagonal of the upper triangle.
    format : string
        Sparse format of the result, e.g. format="csr", etc.

    Returns
    -------
    L : sparse array or matrix
        Upper triangular portion of A in sparse format.
        Sparse array if A is a sparse array, otherwise matrix.

    See Also
    --------
    tril : lower triangle in sparse format

    Examples
    --------
    >>> from scipy.sparse import csr_array, triu
    >>> A = csr_array([[1, 2, 0, 0, 3], [4, 5, 0, 6, 7], [0, 0, 8, 9, 0]],
    ...                dtype='int32')
    >>> A.toarray()
    array([[1, 2, 0, 0, 3],
           [4, 5, 0, 6, 7],
           [0, 0, 8, 9, 0]], dtype=int32)
    >>> triu(A).toarray()
    array([[1, 2, 0, 0, 3],
           [0, 5, 0, 6, 7],
           [0, 0, 8, 9, 0]], dtype=int32)
    >>> triu(A).nnz
    8
    >>> triu(A, k=1).toarray()
    array([[0, 2, 0, 0, 3],
           [0, 0, 0, 6, 7],
           [0, 0, 0, 9, 0]], dtype=int32)
    >>> triu(A, k=-1).toarray()
    array([[1, 2, 0, 0, 3],
           [4, 5, 0, 6, 7],
           [0, 0, 8, 9, 0]], dtype=int32)
    >>> triu(A, format='csc')
    <Compressed Sparse Column sparse array of dtype 'int32'
        with 8 stored elements and shape (3, 5)>

    """
    ...

