"""
This type stub file was generated by pyright.
"""

from scipy._lib._sparse import SparseABC

"""Base class for sparse matrices"""
__all__ = ['isspmatrix', 'issparse', 'sparray', 'SparseWarning', 'SparseEfficiencyWarning']
class SparseWarning(Warning):
    """General warning for :mod:`scipy.sparse`."""
    ...


class SparseFormatWarning(SparseWarning):
    ...


class SparseEfficiencyWarning(SparseWarning):
    """The warning emitted when the operation is
    inefficient for sparse matrices.
    """
    ...


_formats = ...
_ufuncs_with_fixed_point_at_zero = ...
MAXPRINT = ...
op_neg = ...
op_sym = ...
class _spbase(SparseABC):
    """ This class provides a base class for all sparse arrays.  It
    cannot be instantiated.  Most of the work is provided by subclasses.
    """
    __array_priority__ = ...
    _format = ...
    _allow_nd = ...
    @property
    def ndim(self) -> int:
        ...
    
    def __init__(self, arg1, *, maxprint=...) -> None:
        ...
    
    @property
    def shape(self): # -> None:
        ...
    
    def reshape(self, *args, **kwargs): # -> Self:
        """reshape(self, shape, order='C', copy=False)

        Gives a new shape to a sparse array/matrix without changing its data.

        Parameters
        ----------
        shape : tuple of ints
            The new shape should be compatible with the original shape.
        order : {'C', 'F'}, optional
            Read the elements using this index order. 'C' means to read and
            write the elements using C-like index order; e.g., read entire first
            row, then second row, etc. 'F' means to read and write the elements
            using Fortran-like index order; e.g., read entire first column, then
            second column, etc.
        copy : bool, optional
            Indicates whether or not attributes of self should be copied
            whenever possible. The degree to which attributes are copied varies
            depending on the type of sparse array being used.

        Returns
        -------
        reshaped : sparse array/matrix
            A sparse array/matrix with the given `shape`, not necessarily of the same
            format as the current object.

        See Also
        --------
        numpy.reshape : NumPy's implementation of 'reshape' for ndarrays
        """
        ...
    
    def resize(self, shape):
        """Resize the array/matrix in-place to dimensions given by ``shape``

        Any elements that lie within the new shape will remain at the same
        indices, while non-zero elements lying outside the new shape are
        removed.

        Parameters
        ----------
        shape : (int, int)
            number of rows and columns in the new array/matrix

        Notes
        -----
        The semantics are not identical to `numpy.ndarray.resize` or
        `numpy.resize`. Here, the same data will be maintained at each index
        before and after reshape, if that index is within the new bounds. In
        numpy, resizing maintains contiguity of the array, moving elements
        around in the logical array but not within a flattened representation.

        We give no guarantees about whether the underlying data attributes
        (arrays, etc.) will be modified in place or replaced with new objects.
        """
        ...
    
    def astype(self, dtype, casting=..., copy=...): # -> Self:
        """Cast the array/matrix elements to a specified type.

        Parameters
        ----------
        dtype : string or numpy dtype
            Typecode or data-type to which to cast the data.
        casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
            Controls what kind of data casting may occur.
            Defaults to 'unsafe' for backwards compatibility.
            'no' means the data types should not be cast at all.
            'equiv' means only byte-order changes are allowed.
            'safe' means only casts which can preserve values are allowed.
            'same_kind' means only safe casts or casts within a kind,
            like float64 to float32, are allowed.
            'unsafe' means any data conversions may be done.
        copy : bool, optional
            If `copy` is `False`, the result might share some memory with this
            array/matrix. If `copy` is `True`, it is guaranteed that the result and
            this array/matrix do not share any memory.
        """
        ...
    
    def __iter__(self): # -> Generator[Any, Any, None]:
        ...
    
    def count_nonzero(self, axis=...):
        """Number of non-zero entries, equivalent to

        np.count_nonzero(a.toarray(), axis=axis)

        Unlike the nnz property, which return the number of stored
        entries (the length of the data attribute), this method counts the
        actual number of non-zero entries in data.

        Duplicate entries are summed before counting.

        Parameters
        ----------
        axis : {-2, -1, 0, 1, None} optional
            Count nonzeros for the whole array, or along a specified axis.

            .. versionadded:: 1.15.0

        Returns
        -------
        numpy array
            A reduced array (no axis `axis`) holding the number of nonzero values
            for each of the indices of the nonaxis dimensions.

        Notes
        -----
        If you want to count nonzero and explicit zero stored values (e.g. nnz)
        along an axis, two fast idioms are provided by `numpy` functions for the
        common CSR, CSC, COO formats.

        For the major axis in CSR (rows) and CSC (cols) use `np.diff`:

            >>> import numpy as np
            >>> import scipy as sp
            >>> A = sp.sparse.csr_array([[4, 5, 0], [7, 0, 0]])
            >>> major_axis_stored_values = np.diff(A.indptr)  # -> np.array([2, 1])

        For the minor axis in CSR (cols) and CSC (rows) use `numpy.bincount` with
        minlength ``A.shape[1]`` for CSR and ``A.shape[0]`` for CSC:

            >>> csr_minor_stored_values = np.bincount(A.indices, minlength=A.shape[1])

        For COO, use the minor axis approach for either `axis`:

            >>> A = A.tocoo()
            >>> coo_axis0_stored_values = np.bincount(A.coords[0], minlength=A.shape[1])
            >>> coo_axis1_stored_values = np.bincount(A.coords[1], minlength=A.shape[0])

        Examples
        --------

            >>> A = sp.sparse.csr_array([[4, 5, 0], [7, 0, 0]])
            >>> A.count_nonzero(axis=0)
            array([2, 1, 0])
        """
        ...
    
    @property
    def nnz(self) -> int:
        """Number of stored values, including explicit zeros.

        See also
        --------
        count_nonzero : Number of non-zero entries
        """
        ...
    
    @property
    def size(self) -> int:
        """Number of stored values.

        See also
        --------
        count_nonzero : Number of non-zero values.
        """
        ...
    
    @property
    def format(self) -> str:
        """Format string for matrix."""
        ...
    
    @property
    def T(self):
        """Transpose."""
        ...
    
    @property
    def real(self):
        ...
    
    @property
    def imag(self):
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    __nonzero__ = ...
    def __len__(self):
        ...
    
    def asformat(self, format, copy=...): # -> Self | Any:
        """Return this array/matrix in the passed format.

        Parameters
        ----------
        format : {str, None}
            The desired sparse format ("csr", "csc", "lil", "dok", "array", ...)
            or None for no conversion.
        copy : bool, optional
            If True, the result is guaranteed to not share data with self.

        Returns
        -------
        A : This array/matrix in the passed format.
        """
        ...
    
    def multiply(self, other): # -> _NotImplementedType | Self:
        """Element-wise multiplication by another array/matrix."""
        ...
    
    def maximum(self, other): # -> Self:
        """Element-wise maximum between this and another array/matrix."""
        ...
    
    def minimum(self, other): # -> Self:
        """Element-wise minimum between this and another array/matrix."""
        ...
    
    def dot(self, other): # -> _NotImplementedType | Self:
        """Ordinary dot product

        Examples
        --------
        >>> import numpy as np
        >>> from scipy.sparse import csr_array
        >>> A = csr_array([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
        >>> v = np.array([1, 0, -1])
        >>> A.dot(v)
        array([ 1, -3, -1], dtype=int64)

        """
        ...
    
    def power(self, n, dtype=...):
        """Element-wise power."""
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __abs__(self):
        ...
    
    def __round__(self, ndigits=...):
        ...
    
    def __add__(self, other): # -> Self | _NotImplementedType:
        ...
    
    def __radd__(self, other): # -> Self | _NotImplementedType:
        ...
    
    def __sub__(self, other): # -> Self | _NotImplementedType:
        ...
    
    def __rsub__(self, other): # -> _NotImplementedType:
        ...
    
    def __mul__(self, other): # -> _NotImplementedType | Self:
        ...
    
    def __rmul__(self, other): # -> _NotImplementedType | Self:
        ...
    
    def __matmul__(self, other): # -> _NotImplementedType | ndarray[tuple[int], dtype[Any]] | ndarray[tuple[int], Any] | ndarray[tuple[int, int], dtype[Any]] | ndarray[tuple[int, int], Any] | NDArray[Any] | matrix[Any, Any]:
        ...
    
    def __rmatmul__(self, other): # -> _NotImplementedType:
        ...
    
    def __truediv__(self, other): # -> _NotImplementedType | NDArray[Any] | Self:
        ...
    
    def __div__(self, other): # -> _NotImplementedType | NDArray[Any] | Self:
        ...
    
    def __rtruediv__(self, other): # -> _NotImplementedType:
        ...
    
    def __rdiv__(self, other): # -> _NotImplementedType:
        ...
    
    def __neg__(self):
        ...
    
    def __iadd__(self, other): # -> _NotImplementedType:
        ...
    
    def __isub__(self, other): # -> _NotImplementedType:
        ...
    
    def __imul__(self, other): # -> _NotImplementedType:
        ...
    
    def __idiv__(self, other): # -> _NotImplementedType:
        ...
    
    def __itruediv__(self, other): # -> _NotImplementedType:
        ...
    
    def __pow__(self, *args, **kwargs):
        ...
    
    def transpose(self, axes=..., copy=...):
        """
        Reverses the dimensions of the sparse array/matrix.

        Parameters
        ----------
        axes : None, optional
            This argument is in the signature *solely* for NumPy
            compatibility reasons. Do not pass in anything except
            for the default value.
        copy : bool, optional
            Indicates whether or not attributes of `self` should be
            copied whenever possible. The degree to which attributes
            are copied varies depending on the type of sparse array/matrix
            being used.

        Returns
        -------
        p : `self` with the dimensions reversed.

        Notes
        -----
        If `self` is a `csr_array` or a `csc_array`, then this will return a
        `csc_array` or a `csr_array`, respectively.

        See Also
        --------
        numpy.transpose : NumPy's implementation of 'transpose' for ndarrays
        """
        ...
    
    def conjugate(self, copy=...): # -> Self:
        """Element-wise complex conjugation.

        If the array/matrix is of non-complex data type and `copy` is False,
        this method does nothing and the data is not copied.

        Parameters
        ----------
        copy : bool, optional
            If True, the result is guaranteed to not share data with self.

        Returns
        -------
        A : The element-wise complex conjugate.

        """
        ...
    
    def conj(self, copy=...): # -> Self:
        ...
    
    def nonzero(self): # -> tuple[Any, ...]:
        """Nonzero indices of the array/matrix.

        Returns a tuple of arrays (row,col) containing the indices
        of the non-zero elements of the array.

        Examples
        --------
        >>> from scipy.sparse import csr_array
        >>> A = csr_array([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
        >>> A.nonzero()
        (array([0, 0, 1, 2, 2], dtype=int32), array([0, 1, 2, 0, 2], dtype=int32))

        """
        ...
    
    def todense(self, order=..., out=...): # -> NDArray[Any] | matrix[Any, Any]:
        """
        Return a dense representation of this sparse array.

        Parameters
        ----------
        order : {'C', 'F'}, optional
            Whether to store multi-dimensional data in C (row-major)
            or Fortran (column-major) order in memory. The default
            is 'None', which provides no ordering guarantees.
            Cannot be specified in conjunction with the `out`
            argument.

        out : ndarray, 2-D, optional
            If specified, uses this array as the output buffer
            instead of allocating a new array to return. The
            provided array must have the same shape and dtype as
            the sparse array on which you are calling the method.

        Returns
        -------
        arr : ndarray, 2-D
            An array with the same shape and containing the same
            data represented by the sparse array, with the requested
            memory order. If `out` was passed, the same object is
            returned after being modified in-place to contain the
            appropriate values.
        """
        ...
    
    def toarray(self, order=..., out=...):
        """
        Return a dense ndarray representation of this sparse array/matrix.

        Parameters
        ----------
        order : {'C', 'F'}, optional
            Whether to store multidimensional data in C (row-major)
            or Fortran (column-major) order in memory. The default
            is 'None', which provides no ordering guarantees.
            Cannot be specified in conjunction with the `out`
            argument.

        out : ndarray, 2-D, optional
            If specified, uses this array as the output buffer
            instead of allocating a new array to return. The provided
            array must have the same shape and dtype as the sparse
            array/matrix on which you are calling the method. For most
            sparse types, `out` is required to be memory contiguous
            (either C or Fortran ordered).

        Returns
        -------
        arr : ndarray, 2-D
            An array with the same shape and containing the same
            data represented by the sparse array/matrix, with the requested
            memory order. If `out` was passed, the same object is
            returned after being modified in-place to contain the
            appropriate values.
        """
        ...
    
    def tocsr(self, copy=...):
        """Convert this array/matrix to Compressed Sparse Row format.

        With copy=False, the data/indices may be shared between this array/matrix and
        the resultant csr_array/matrix.
        """
        ...
    
    def todok(self, copy=...):
        """Convert this array/matrix to Dictionary Of Keys format.

        With copy=False, the data/indices may be shared between this array/matrix and
        the resultant dok_array/matrix.
        """
        ...
    
    def tocoo(self, copy=...):
        """Convert this array/matrix to COOrdinate format.

        With copy=False, the data/indices may be shared between this array/matrix and
        the resultant coo_array/matrix.
        """
        ...
    
    def tolil(self, copy=...):
        """Convert this array/matrix to List of Lists format.

        With copy=False, the data/indices may be shared between this array/matrix and
        the resultant lil_array/matrix.
        """
        ...
    
    def todia(self, copy=...):
        """Convert this array/matrix to sparse DIAgonal format.

        With copy=False, the data/indices may be shared between this array/matrix and
        the resultant dia_array/matrix.
        """
        ...
    
    def tobsr(self, blocksize=..., copy=...):
        """Convert this array/matrix to Block Sparse Row format.

        With copy=False, the data/indices may be shared between this array/matrix and
        the resultant bsr_array/matrix.

        When blocksize=(R, C) is provided, it will be used for construction of
        the bsr_array/matrix.
        """
        ...
    
    def tocsc(self, copy=...):
        """Convert this array/matrix to Compressed Sparse Column format.

        With copy=False, the data/indices may be shared between this array/matrix and
        the resultant csc_array/matrix.
        """
        ...
    
    def copy(self): # -> Self:
        """Returns a copy of this array/matrix.

        No data/indices will be shared between the returned value and current
        array/matrix.
        """
        ...
    
    def sum(self, axis=..., dtype=..., out=...): # -> NDArray[Any] | matrix[Any, Any]:
        """
        Sum the array/matrix elements over a given axis.

        Parameters
        ----------
        axis : {-2, -1, 0, 1, None} optional
            Axis along which the sum is computed. The default is to
            compute the sum of all the array/matrix elements, returning a scalar
            (i.e., `axis` = `None`).
        dtype : dtype, optional
            The type of the returned array/matrix and of the accumulator in which
            the elements are summed.  The dtype of `a` is used by default
            unless `a` has an integer dtype of less precision than the default
            platform integer.  In that case, if `a` is signed then the platform
            integer is used while if `a` is unsigned then an unsigned integer
            of the same precision as the platform integer is used.

            .. versionadded:: 0.18.0

        out : np.matrix, optional
            Alternative output matrix in which to place the result. It must
            have the same shape as the expected output, but the type of the
            output values will be cast if necessary.

            .. versionadded:: 0.18.0

        Returns
        -------
        sum_along_axis : np.matrix
            A matrix with the same shape as `self`, with the specified
            axis removed.

        See Also
        --------
        numpy.matrix.sum : NumPy's implementation of 'sum' for matrices

        """
        ...
    
    def mean(self, axis=..., dtype=..., out=...): # -> ndarray[_Shape, dtype[Any]] | ndarray[Any, dtype[Any]] | Any | matrix[Any, Any]:
        """
        Compute the arithmetic mean along the specified axis.

        Returns the average of the array/matrix elements. The average is taken
        over all elements in the array/matrix by default, otherwise over the
        specified axis. `float64` intermediate and return values are used
        for integer inputs.

        Parameters
        ----------
        axis : {-2, -1, 0, 1, None} optional
            Axis along which the mean is computed. The default is to compute
            the mean of all elements in the array/matrix (i.e., `axis` = `None`).
        dtype : data-type, optional
            Type to use in computing the mean. For integer inputs, the default
            is `float64`; for floating point inputs, it is the same as the
            input dtype.

            .. versionadded:: 0.18.0

        out : np.matrix, optional
            Alternative output matrix in which to place the result. It must
            have the same shape as the expected output, but the type of the
            output values will be cast if necessary.

            .. versionadded:: 0.18.0

        Returns
        -------
        m : np.matrix

        See Also
        --------
        numpy.matrix.mean : NumPy's implementation of 'mean' for matrices

        """
        ...
    
    def diagonal(self, k=...):
        """Returns the kth diagonal of the array/matrix.

        Parameters
        ----------
        k : int, optional
            Which diagonal to get, corresponding to elements a[i, i+k].
            Default: 0 (the main diagonal).

            .. versionadded:: 1.0

        See also
        --------
        numpy.diagonal : Equivalent numpy function.

        Examples
        --------
        >>> from scipy.sparse import csr_array
        >>> A = csr_array([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
        >>> A.diagonal()
        array([1, 0, 5])
        >>> A.diagonal(k=1)
        array([2, 3])
        """
        ...
    
    def trace(self, offset=...):
        """Returns the sum along diagonals of the sparse array/matrix.

        Parameters
        ----------
        offset : int, optional
            Which diagonal to get, corresponding to elements a[i, i+offset].
            Default: 0 (the main diagonal).

        """
        ...
    
    def setdiag(self, values, k=...): # -> None:
        """
        Set diagonal or off-diagonal elements of the array/matrix.

        Parameters
        ----------
        values : array_like
            New values of the diagonal elements.

            Values may have any length. If the diagonal is longer than values,
            then the remaining diagonal entries will not be set. If values are
            longer than the diagonal, then the remaining values are ignored.

            If a scalar value is given, all of the diagonal is set to it.

        k : int, optional
            Which off-diagonal to set, corresponding to elements a[i,i+k].
            Default: 0 (the main diagonal).

        """
        ...
    


class sparray:
    """A namespace class to separate sparray from spmatrix"""
    @classmethod
    def __class_getitem__(cls, arg, /): # -> GenericAlias:
        """
        Return a parametrized wrapper around the `~scipy.sparse.sparray` type.

        .. versionadded:: 1.16.0

        Returns
        -------
        alias : types.GenericAlias
            A parametrized `~scipy.sparse.sparray` type.

        Examples
        --------
        >>> import numpy as np
        >>> from scipy.sparse import coo_array

        >>> coo_array[np.int8, tuple[int]]
        scipy.sparse._coo.coo_array[numpy.int8, tuple[int]]
        """
        ...
    


def isspmatrix(x): # -> bool:
    """Is `x` of a sparse matrix type?

    Parameters
    ----------
    x
        object to check for being a sparse matrix

    Returns
    -------
    bool
        True if `x` is a sparse matrix, False otherwise

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import csr_array, csr_matrix, isspmatrix
    >>> isspmatrix(csr_matrix([[5]]))
    True
    >>> isspmatrix(csr_array([[5]]))
    False
    >>> isspmatrix(np.array([[5]]))
    False
    >>> isspmatrix(5)
    False
    """
    ...

